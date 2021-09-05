import os
import re
import argparse
import Bio.SeqIO as sio 
import numpy as np
from outcyte_sp import run_sp
from outcyte_ups import run_ups
import warnings
warnings.filterwarnings("ignore")

def run_file():
    parser = argparse.ArgumentParser()
    parser.add_argument('fasta_file', type=str)
    parser.add_argument('method', type=str)
    args = parser.parse_args()
    ids, seqs = fasta_reader(args.fasta_file)
    #method = 'outcyte-ups'
    name = args.fasta_file.split('/')[-1].split('.')[0]
    res = run(ids, seqs, args.method, name)
    #print(res)
    return res

def fasta_reader(inputs):
    records = sio.parse(inputs, 'fasta')
    ids = []
    seqs = []
    for r in records:
        seq = str(r.seq)
        if len(seq) < 20:
            continue
        seqs.append(seq)
        ids.append(str(r.id))
    return ids, seqs

def run(seqID, seqs, method, fname):
    """API to take user input data from the frontend"""

    #seqID, seqs = read_fasta_alt(inputs, splitter)
    if len(seqs) > 100000:
        return "Maximal number of sequences is 100."
    #while '\r' in seqs or '\n' in seqs:
    #    seqs.remove('\r')
    else:
        if method == 'outcyte-sp':
            res = run_sp(seqID, seqs, fname)
        elif method == 'outcyte-ups':
            res = run_ups(seqID, seqs, fname)
        else:
            fname = fname + '_pipeline'
            res_sp = run_sp(seqID, seqs, fname)
            pred_class = res_sp[:, 1]
            nc_index = (pred_class == 'Intracellular').nonzero()[0]
            #print(nc_index)
            if len(nc_index) == 0:
                return res_sp
            else:
                id_nc, seq_nc = [seqID[i] for i in nc_index], [seqs[i] for i in nc_index]
                res_ups = run_ups(id_nc, seq_nc, fname)
                res_sp[nc_index] = res_ups
                res = res_sp
            if not os.path.isdir('./results'):
                os.makedirs('./results/', exist_ok=True)
            np.savetxt(
                './results/{}.txt'.format(fname),
                res,
                fmt='%s'
            )
        return res

def read_fasta(inputs):
    res = re.findall(r">.*?\n|(?:[^>].*?\n)+", inputs)
    ids = res[0::2]
    seqs = res[1::2]
    ids = [i.split(' ')[0].split('>')[1] if (' ' in i) == True else i[1:-1] for i in ids]
    seqs = [('').join(i.split('\n')) for i in seqs]
    return ids, seqs

def read_fasta_alt(inputs, splitter):
    res = inputs.split(splitter)
    seq_index = [i for i in range(len(res)) if res[i].startswith('>')]
    describe_line = [res[i] for i in seq_index]
    ids = [i.split(' ')[0].split('>')[1] if (' ' in i) == True else i[1:-1] for i in describe_line]
    num_seq = len(describe_line)
    if num_seq == 1:
        seqs = [''.join(res[1:])]
    else:
        seqs = []
        seq_index = seq_index + [len(res)]
        for k in range(len(seq_index)-1):
            current_des = seq_index[k]+1
            next_des = seq_index[k+1]
            #print('the range', current_des, next_des)
            s = ''.join([res[i] for i in range(current_des, next_des)])
            #print('s', s)
            seqs.append(s)
    #print('seq', seqs)
    return ids, seqs

if __name__ == '__main__':
    run_file()
