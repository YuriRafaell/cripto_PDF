import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfWriter, PdfReader

def proteger_pdf(arquivo_pdf, arquivo_pdf_protegido, senha):
    pdf_writer = PdfWriter()
    pdf_reader = PdfReader(arquivo_pdf)

    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    pdf_writer.encrypt(senha)

    with open(arquivo_pdf_protegido, 'wb') as f:
        pdf_writer.write(f)

    messagebox.showinfo("Sucesso", f"O PDF {arquivo_pdf_protegido} foi criado e protegido com senha.")

def selecionar_arquivo():
    arquivo_pdf = filedialog.askopenfilename(title="Selecione o arquivo PDF",
                                             filetypes=[("PDF files", "*.pdf")])
    if arquivo_pdf:
        entry_arquivo_pdf.delete(0, tk.END)
        entry_arquivo_pdf.insert(0, arquivo_pdf)

def processar():
    arquivo_pdf = entry_arquivo_pdf.get()
    nome_do_doc = entry_nome_do_doc.get()
    senha = entry_senha.get()

    if not arquivo_pdf or not nome_do_doc or not senha:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        return

    arquivo_pdf_protegido = f"{nome_do_doc}.pdf"
    proteger_pdf(arquivo_pdf, arquivo_pdf_protegido, senha)

root = tk.Tk()
root.title("Protegendo seu documento")

# Definindo altura e largura da janela
window_width = 1400
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Add a header
header = tk.Label(root, text="Protegendo seu documento", fg='white', font=('Arial', 20, 'bold'))
header.pack(fill=tk.X, pady=10)

# Frame for form
frame = tk.Frame(root, bg='#f0f0f0')
frame.pack(pady=20, padx=20)

# Nome do Arquivo PDF
label_arquivo_pdf = tk.Label(frame, text="Arquivo PDF:", bg='#f0f0f0', font=('Arial', 12))
label_arquivo_pdf.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
entry_arquivo_pdf = tk.Entry(frame, width=40, font=('Arial', 12))
entry_arquivo_pdf.grid(row=0, column=1, padx=10, pady=5)

# Botão Selecionar
btn_selecionar = tk.Button(frame, text="Selecionar", command=selecionar_arquivo, font=('Arial', 12), bg='#4a90e2', fg='white')
btn_selecionar.grid(row=0, column=2, padx=10, pady=5)

# Nome do Arquivo Protegido
label_nome_do_doc = tk.Label(frame, text="Nome do Arquivo Protegido:", bg='#f0f0f0', font=('Arial', 12))
label_nome_do_doc.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
entry_nome_do_doc = tk.Entry(frame, width=40, font=('Arial', 12))
entry_nome_do_doc.grid(row=1, column=1, padx=10, pady=5, columnspan=2)

# Senha
label_senha = tk.Label(frame, text="Senha:", bg='#f0f0f0', font=('Arial', 12))
label_senha.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
entry_senha = tk.Entry(frame, show='*', width=40, font=('Arial', 12))
entry_senha.grid(row=2, column=1, padx=10, pady=5, columnspan=2)

# Botão Processar
btn_processar = tk.Button(root, text="Proteger PDF", command=processar, font=('Arial', 12, 'bold'), bg='#4a90e2', fg='white')
btn_processar.pack(pady=20)

# Centralizar widgets verticalmente
frame.grid_rowconfigure(3, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(3, weight=1)

root.mainloop()