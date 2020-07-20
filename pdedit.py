import PyPDF2 as pdf
import argparse
import sys 

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parser = argparse.ArgumentParser(prog="Free Pdf Merger", description="This command line tool is a pdf merger."
                                     "List all pdfs you want merged and the order you want them merged", allow_abbrev=True, add_help=True)
    parser.add_argument("pdf", type=str, help="List full pdf names in the order you want them to appear", nargs="+", metavar="N")
    parser.add_argument("-o", "--output", type=str, help="Name for the new pdf made from merging the ones given", dest="name", metavar="file.pdf")
    results = parser.parse_args(args)
    if results.name is None:
        merge_pdfs(results.pdf)
    else:
        merge_pdfs(results.pdf, results.name)

def merge_pdfs(pdf_names: list, output_file="merged_output.pdf"):
    merger = pdf.PdfFileMerger()
    for f in pdf_names:
        merger.append(f)
    merger.write(output_file)

if __name__ == "__main__":
    main()