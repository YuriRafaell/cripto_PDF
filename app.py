import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
import os

# Função para converter TXT para PDF
def converter_txt_para_pdf(arquivo_txt, arquivo_pdf):
    try:
        with open(arquivo_txt, 'r') as f:
            conteudo = f.readlines()

        c = canvas.Canvas(arquivo_pdf)
        largura, altura = 595.27, 841.89  # Tamanho A4 em pontos
        y = altura - 40

        for linha in conteudo:
            if y < 40:  # Verifica se precisa de uma nova página
                c.showPage()
                y = altura - 40
            c.drawString(40, y, linha.strip())
            y -= 15  # Ajuste de espaçamento entre as linhas

        c.save()
        return True
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao converter TXT para PDF: {str(e)}")
        return False

# Função para proteger arquivos PDF
def proteger_pdf(arquivo_pdf, arquivo_pdf_protegido, senha):
    pdf_writer = PdfWriter()
    pdf_reader = PdfReader(arquivo_pdf)

    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    pdf_writer.encrypt(senha)

    with open(arquivo_pdf_protegido, 'wb') as f:
        pdf_writer.write(f)

    # Remover o arquivo original
    os.remove(arquivo_pdf)

# Função para escolher arquivo
def selecionar_arquivo():
    arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo",
        filetypes=[
            ("Arquivos de Texto", "*.txt"),
            ("Arquivos PDF", "*.pdf")
        ]
    )
    if arquivo:
        entry_arquivo.delete(0, tk.END)
        entry_arquivo.insert(0, arquivo)

def processar():
    arquivo = entry_arquivo.get()
    nome_do_doc = entry_nome_do_doc.get()
    senha = entry_senha.get()

    if not arquivo or not nome_do_doc or not senha:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        return

    try:
        extensao = arquivo.lower().split('.')[-1]
        arquivo_protegido = f"{nome_do_doc}.pdf"

        if extensao == 'txt':
            # Converte TXT para PDF
            pdf_temporario = f"{nome_do_doc}_temp.pdf"
            if converter_txt_para_pdf(arquivo, pdf_temporario):
                proteger_pdf(pdf_temporario, arquivo_protegido, senha)
                messagebox.showinfo("Sucesso", f"O arquivo TXT foi convertido e protegido com senha: {arquivo_protegido}")
        elif extensao == 'pdf':
            proteger_pdf(arquivo, arquivo_protegido, senha)
            messagebox.showinfo("Sucesso", f"O PDF foi protegido com senha: {arquivo_protegido}")
        else:
            messagebox.showerror("Erro", "Formato de arquivo não suportado!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao processar o arquivo: {str(e)}")

root = tk.Tk()
root.title("Converter e Proteger Arquivos")

# Configuração da janela
window_width = 1400
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Cabeçalho
header = tk.Label(root, text="Converter TXT para PDF e Proteger", fg='black', font=('Arial', 30, 'bold'))
header.pack(fill=tk.X, pady=50)

# Frame para o formulário
frame = tk.Frame(root, bg='#f0f0f0')
frame.pack(pady=20, padx=20)

# Arquivo
label_arquivo = tk.Label(frame, text="Arquivo:", bg='#f0f0f0', font=('Arial', 15))
label_arquivo.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
entry_arquivo = tk.Entry(frame, width=40, font=('Arial', 12))
entry_arquivo.grid(row=0, column=1, padx=10, pady=5)

# Botão Selecionar
btn_selecionar = tk.Button(frame, text="Selecionar", command=selecionar_arquivo, font=('Arial', 12), bg='#4a90e2', fg='white')
btn_selecionar.grid(row=0, column=2, padx=10, pady=5)

# Nome do Arquivo Protegido
label_nome_do_doc = tk.Label(frame, text="Nome do Arquivo Protegido:", bg='#f0f0f0', font=('Arial', 15))
label_nome_do_doc.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
entry_nome_do_doc = tk.Entry(frame, width=40, font=('Arial', 12))
entry_nome_do_doc.grid(row=1, column=1, padx=10, pady=5, columnspan=2)

# Senha
label_senha = tk.Label(frame, text="Senha:", bg='#f0f0f0', font=('Arial', 15))
label_senha.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
entry_senha = tk.Entry(frame, show='*', width=40, font=('Arial', 12))
entry_senha.grid(row=2, column=1, padx=10, pady=5, columnspan=2)

# Botão Processar
btn_processar = tk.Button(root, text="Converter e Proteger", command=processar, font=('Arial', 15, 'bold'), bg='#4a90e2', fg='white')
btn_processar.pack(pady=20)

root.mainloop()
