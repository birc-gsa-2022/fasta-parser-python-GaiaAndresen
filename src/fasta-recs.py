import argparse

def main():
    argparser = argparse.ArgumentParser(
        description="Extract Simple-FASTA records"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()

    # print(f"Now I need to process the records in {args.fasta}")


    #Assume resonable file

    for e in args.fasta.read().split(">")[1:]:
        name, seq = e.split("\n", 1)
        print(name.strip(), seq.replace("\n", "").strip(), sep='\t')


    #Alternative version
    # seq = ""
    # for e in args.fasta:
    #     if e[0]== '>':
    #         if len(seq)>0:
    #             print(seq)
    #         seq = f'{e[1:].strip()}\t'
    #     else: 
    #         seq = seq + e.strip()
    # print(seq)


if __name__ == '__main__':
    main()
