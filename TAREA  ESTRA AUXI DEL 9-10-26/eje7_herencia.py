import copy



class Documento:
    def __init__(self, titulo: str, autores: list, editorial: str, anio_publicacion: int):
        self.titulo = titulo
        self.autores = autores
        self.editorial = editorial
        self.anio_publicacion = anio_publicacion

    def __str__(self):
        return f"{self.__class__.__name__}: '{self.titulo}'"


class LibroPapel(Documento):
    pass  


class RevistaPapel(LibroPapel):
    def __init__(self, titulo: str, autores: list, editorial: str, anio_publicacion: int, volumen: int, numero: int, mes_salida: str):
        super().__init__(titulo, autores, editorial, anio_publicacion)
        self.volumen = volumen
        self.numero = numero
        self.mes_salida = mes_salida


class DocumentoCD(Documento):
    def __init__(self, titulo: str, autores: list, editorial: str, anio_publicacion: int, formato_cd: str, tipo_licencia: str):
        super().__init__(titulo, autores, editorial, anio_publicacion)
        self.formato_cd = formato_cd
        self.tipo_licencia = tipo_licencia


class RevistaInvestigacion(Documento):
    def __init__(self, titulo: str, autores: list, editorial: str, anio_publicacion: int, campo_investigacion: str):
        super().__init__(titulo, autores, editorial, anio_publicacion)
        self.campo_investigacion = campo_investigacion




class Biblioteca:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.catalogo = []

    def agregar_documento(self, doc: Documento):
        self.catalogo.append(doc)

    def contar_revistas(self) -> int:
        return sum(1 for doc in self.catalogo if isinstance(doc, (RevistaPapel, RevistaInvestigacion)))

    def contar_documentos(self) -> int:
        return len(self.catalogo)

    def contar_libros(self) -> int:
        return sum(1 for doc in self.catalogo if isinstance(doc, LibroPapel) and not isinstance(doc, RevistaPapel))

    def mostrar_catalogo(self):
        print(f"--- Catálogo de {self.nombre} ---")
        if not self.catalogo:
            print("  [Vacío]")
        for doc in self.catalogo:
            print(f"  - {doc}")




libro1 = LibroPapel("El Quijote", ["Cervantes"], "Planeta", 1605)
libro2 = LibroPapel("Cien Años de Soledad", ["García Márquez"], "Sudamericana", 1967)
revista_p1 = RevistaPapel("National Geographic", ["Varios"], "RBA", 2026, 50, 4, "Octubre")
revista_p2 = RevistaPapel("Time", ["Varios"], "Time Inc", 2025, 12, 1, "Enero")
revista_inv = RevistaInvestigacion("AI & Quantum Computing", ["Dr. Smith"], "IEEE", 2026, "Informática")
cd1 = DocumentoCD("Ubuntu Linux OS", ["Canonical"], "Open Source", 2024, "ISO", "GPL")

print("\n=== INCISO B ===")
biblio1 = Biblioteca("Biblioteca Central")
biblio2 = Biblioteca("Biblioteca de Ciencias")

biblio1.agregar_documento(libro1)
biblio1.agregar_documento(revista_p1)
biblio1.agregar_documento(cd1)

biblio2.agregar_documento(libro2)
biblio2.agregar_documento(revista_p2)
biblio2.agregar_documento(revista_inv)

def comparar_bibliotecas(b1: Biblioteca, b2: Biblioteca):
    r1, r2 = b1.contar_revistas(), b2.contar_revistas()
    if r1 > r2:
        print(f"-> {b1.nombre} tiene más revistas ({r1}) que {b2.nombre} ({r2}).")
    elif r2 > r1:
        print(f"-> {b2.nombre} tiene más revistas ({r2}) que {b1.nombre} ({r1}).")
    else:
        print(f"-> Ambas bibliotecas tienen la misma cantidad de revistas ({r1}).")

    d1, d2 = b1.contar_documentos(), b2.contar_documentos()
    if d1 > d2:
        print(f"-> {b1.nombre} tiene más documentos totales ({d1}) que {b2.nombre} ({d2}).")
    elif d2 > d1:
        print(f"-> {b2.nombre} tiene más documentos totales ({d2}) que {b1.nombre} ({d1}).")
    else:
        print(f"-> Ambas bibliotecas tienen los mismos documentos totales ({d1}).")

comparar_bibliotecas(biblio1, biblio2)


print("\n=== INCISO C ===")
print("Efectuando traslado de archivos...")

todos_los_documentos = biblio1.catalogo + biblio2.catalogo
biblio1.catalogo = []
biblio2.catalogo = []

for doc in todos_los_documentos:
    if isinstance(doc, (RevistaPapel, RevistaInvestigacion)):
        biblio1.agregar_documento(doc)
    elif isinstance(doc, LibroPapel) and not isinstance(doc, RevistaPapel):
        biblio2.agregar_documento(doc)
    else:
        print(f"Nota: {doc.titulo} (CD) no clasifica estrictamente como libro o revista para el traslado.")

biblio1.mostrar_catalogo()
biblio2.mostrar_catalogo()


print("\n=== INCISO D ===")
print("Creando copias de seguridad (Deep Copy)...")


backup_biblio1 = copy.deepcopy(biblio1)
backup_biblio2 = copy.deepcopy(biblio2)

backup_biblio1.nombre = "BACKUP - " + biblio1.nombre
backup_biblio2.nombre = "BACKUP - " + biblio2.nombre

backup_biblio1.mostrar_catalogo()
backup_biblio2.mostrar_catalogo()


class Documento:
    def __init__(self, titulo: str, autores: list, editorial: str, anio_publicacion: int):
        self.titulo = titulo
        self.autores = autores
        self.editorial = editorial
        self.anio_publicacion = anio_publicacion

    def __str__(self):
        return f"{self.__class__.__name__}: '{self.titulo}'"


class LibroPapel(Documento):
    pass  


class RevistaPapel(LibroPapel):
    def __init__(self, titulo: str, autores: list, editorial: str, anio_publicacion: int, volumen: int, numero: int, mes_salida: str):
        super().__init__(titulo, autores, editorial, anio_publicacion)
        self.volumen = volumen
        self.numero = numero
        self.mes_salida = mes_salida


class DocumentoCD(Documento):
    def __init__(self, titulo: str, autores: list, editorial: str, anio_publicacion: int, formato_cd: str, tipo_licencia: str):
        super().__init__(titulo, autores, editorial, anio_publicacion)
        self.formato_cd = formato_cd
        self.tipo_licencia = tipo_licencia


class RevistaInvestigacion(Documento):
    def __init__(self, titulo: str, autores: list, editorial: str, anio_publicacion: int, campo_investigacion: str):
        super().__init__(titulo, autores, editorial, anio_publicacion)
        self.campo_investigacion = campo_investigacion




class Biblioteca:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.catalogo = []

    def agregar_documento(self, doc: Documento):
        self.catalogo.append(doc)

    def contar_revistas(self) -> int:
        return sum(1 for doc in self.catalogo if isinstance(doc, (RevistaPapel, RevistaInvestigacion)))

    def contar_documentos(self) -> int:
        return len(self.catalogo)

    def contar_libros(self) -> int:
        return sum(1 for doc in self.catalogo if isinstance(doc, LibroPapel) and not isinstance(doc, RevistaPapel))

    def mostrar_catalogo(self):
        print(f"--- Catálogo de {self.nombre} ---")
        if not self.catalogo:
            print("  [Vacío]")
        for doc in self.catalogo:
            print(f"  - {doc}")




libro1 = LibroPapel("El Quijote", ["Cervantes"], "Planeta", 1605)
libro2 = LibroPapel("Cien Años de Soledad", ["García Márquez"], "Sudamericana", 1967)
revista_p1 = RevistaPapel("National Geographic", ["Varios"], "RBA", 2026, 50, 4, "Octubre")
revista_p2 = RevistaPapel("Time", ["Varios"], "Time Inc", 2025, 12, 1, "Enero")
revista_inv = RevistaInvestigacion("AI & Quantum Computing", ["Dr. Smith"], "IEEE", 2026, "Informática")
cd1 = DocumentoCD("Ubuntu Linux OS", ["Canonical"], "Open Source", 2024, "ISO", "GPL")

print("\n=== INCISO B ===")
biblio1 = Biblioteca("Biblioteca Central")
biblio2 = Biblioteca("Biblioteca de Ciencias")

biblio1.agregar_documento(libro1)
biblio1.agregar_documento(revista_p1)
biblio1.agregar_documento(cd1)

biblio2.agregar_documento(libro2)
biblio2.agregar_documento(revista_p2)
biblio2.agregar_documento(revista_inv)

def comparar_bibliotecas(b1: Biblioteca, b2: Biblioteca):
    r1, r2 = b1.contar_revistas(), b2.contar_revistas()
    if r1 > r2:
        print(f"-> {b1.nombre} tiene más revistas ({r1}) que {b2.nombre} ({r2}).")
    elif r2 > r1:
        print(f"-> {b2.nombre} tiene más revistas ({r2}) que {b1.nombre} ({r1}).")
    else:
        print(f"-> Ambas bibliotecas tienen la misma cantidad de revistas ({r1}).")

    d1, d2 = b1.contar_documentos(), b2.contar_documentos()
    if d1 > d2:
        print(f"-> {b1.nombre} tiene más documentos totales ({d1}) que {b2.nombre} ({d2}).")
    elif d2 > d1:
        print(f"-> {b2.nombre} tiene más documentos totales ({d2}) que {b1.nombre} ({d1}).")
    else:
        print(f"-> Ambas bibliotecas tienen los mismos documentos totales ({d1}).")

comparar_bibliotecas(biblio1, biblio2)


print("\n=== INCISO C ===")
print("Efectuando traslado de archivos...")

todos_los_documentos = biblio1.catalogo + biblio2.catalogo
biblio1.catalogo = []
biblio2.catalogo = []

for doc in todos_los_documentos:
    if isinstance(doc, (RevistaPapel, RevistaInvestigacion)):
        biblio1.agregar_documento(doc)
    elif isinstance(doc, LibroPapel) and not isinstance(doc, RevistaPapel):
        biblio2.agregar_documento(doc)
    else:
        print(f"Nota: {doc.titulo} (CD) no clasifica estrictamente como libro o revista para el traslado.")

biblio1.mostrar_catalogo()
biblio2.mostrar_catalogo()


print("\n=== INCISO D ===")
print("Creando copias de seguridad (Deep Copy)...")


backup_biblio1 = copy.deepcopy(biblio1)
backup_biblio2 = copy.deepcopy(biblio2)

backup_biblio1.nombre = "BACKUP - " + biblio1.nombre
backup_biblio2.nombre = "BACKUP - " + biblio2.nombre

backup_biblio1.mostrar_catalogo()
backup_biblio2.mostrar_catalogo()
