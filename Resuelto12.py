def obtener_tipo_mime(nombre_archivo):
    tipos_mime = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }
    extension = nombre_archivo.lower().split(".")[-1]
    return tipos_mime.get("." + extension, "application/octet-stream")

def main():
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    tipo_mime = obtener_tipo_mime(nombre_archivo)
    print("Tipo MIME:", tipo_mime)

if __name__ == "__main__":
    main()
