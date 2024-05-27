from PyPDF2 import PdfWriter, PdfReader

def proteger_pdf(arquivo_pdf, arquivo_pdf_protegido, senha):
    pdf_writer = PdfWriter()
    pdf_reader = PdfReader(arquivo_pdf)

    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    pdf_writer.encrypt(senha)

    with open(arquivo_pdf_protegido, 'wb') as f:
        pdf_writer.write(f)

# Caminhos dos arquivos
arquivo_pdf = 'teste.pdf'
arquivo_pdf_protegido = 'nome_do_doc.pdf'
senha = 'sua_senha'

proteger_pdf(arquivo_pdf, arquivo_pdf_protegido, senha)

print(f'O PDF {arquivo_pdf_protegido} foi criado e protegido com senha.')
