from reportlab.pdfgen import canvas
from PIL import Image
import os

def convert_jpg_to_pdf(folder_path, pdf_output_path):
    image_files = [f for f in os.listdir(folder_path) if f.endswith(".jpg")] 

    if not image_files:
        print("JPG formatında dosya bulunamadı")
        return
    
    pdf_path = os.path.join(pdf_output_path, "output.pdf") # yeni işlem yaparken output ismini değiştirmelisiniz yoksa üzerine kaydeder eski dosyanız silinir.

    c = canvas.Canvas(pdf_path)

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        img = Image.open(image_path)
        width,height = img.size
        c.setPageSize((width,height))
        c.drawInlineImage(image_path,0 ,0,width, height)

        c.showPage()

    c.save()
    print(f"{pdf_path}.pdf dosyası oluşturuldu")

jpf_folder_path= "donusturulecek_gorseller" # pdf yapmak istediğiniz görseller hangi klasörde bulunuyorsa o klasörün ismini yazmalısınız.
pdf_output_path = "PDF_Formatı"
convert_jpg_to_pdf(jpf_folder_path, pdf_output_path)
