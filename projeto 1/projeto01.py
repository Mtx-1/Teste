from fpdf import FPDF

projeto = input('digite a descrição do projeto: ')
horas_previtas = input('digite a quantidade de horas previstas: ')
valor_hora = input('digite o valor da hora trabalhada: ')
prazo = input('digite o prazo trabalhado: ')

valor_total = int(horas_previtas) * int(valor_hora)

pdf = FPDF()

pdf.add_page()
pdf.set_font('Arial')

pdf.image('foto.png', x=0, y=0)

pdf.text(115, 145, 'Sistema Python')
pdf.text(115, 160, horas_previtas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))

pdf.output('Orçamento.pdf')
print('Orçamento gerado com sucesso!')