import argparse
import sys


def main():
    argparser = argparse.ArgumentParser(
        description="Extract sub-sequences from a Simple-FASTA file"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    argparser.add_argument(
        "coords",
        nargs="?",
        type=argparse.FileType('r'),
        default=sys.stdin
    )
    args = argparser.parse_args()

    # print(f"Now I need to process the records in {args.fasta}")
    # print(f"and the coordinates in {args.coords}")

    seqs = {}
    for e in args.fasta.read().split(">")[1:]:
        name, seq = e.split("\n", 1)
        seqs[name.strip()] = seq.replace("\n", "").strip()
    
    for coor in args.coords:
        name, coor1, coor2 = coor.split()
        print(seqs[name.strip()][int(coor1)-1:int(coor2)-1])


if __name__ == '__main__':
    main()
