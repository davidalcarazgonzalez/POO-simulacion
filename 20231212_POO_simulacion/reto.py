class Curso:
    def __init__(self, id_curso, nombre, creditos, anos_de_estudio):
        self.id = id_curso
        self.nombre = nombre
        self.creditos = creditos
        self.anos_de_estudio = anos_de_estudio

    def mostrar_ficha(self):
        print(f"Ficha del Curso {self.id}: {self.nombre}")
        print(f"Créditos: {self.creditos}")
        print(f"Años de estudio: {self.anos_de_estudio}")
        print()

class Alumno:
    def __init__(self, id_alumno, nombre, email):
        self.id = id_alumno
        self.nombre = nombre
        self.email = email

    def mostrar_ficha(self):
        print(f"Ficha del Alumno {self.id}: {self.nombre}")
        print(f"Email: {self.email}")
        print()

class Matricula:
    def __init__(self, id_matricula, fecha_matricula, id_alumno, id_curso):
        self.id_matricula = id_matricula
        self.fecha_matricula = fecha_matricula
        self.id_alumno = id_alumno
        self.id_curso = id_curso

    def mostrar_datos(self, alumnos, cursos):
        alumno = next(alumno for alumno in alumnos if alumno.id == self.id_alumno)
        curso = next(curso for curso in cursos if curso.id == self.id_curso)

        print(f"Datos de Matrícula {self.id_matricula}")
        print(f"Fecha de matrícula: {self.fecha_matricula}")
        print(f"ID Alumno: {alumno.nombre}")
        print(f"ID Curso: {curso.nombre}")
        print()

class CentroEducativo:
    def __init__(self):
        self.matriculas = []

    def realizar_matricula(self, id_matricula, fecha_matricula, id_alumno, id_curso):
        matricula = Matricula(id_matricula, fecha_matricula, id_alumno, id_curso)
        self.matriculas.append(matricula)

    def mostrar_matriculas(self, alumnos, cursos):
        print("Matrículas realizadas en el centro:")
        for matricula in self.matriculas:
            matricula.mostrar_datos(alumnos, cursos)

curso1 = Curso(1, "Matemáticas", 4, 2)
curso2 = Curso(2, "Historia", 3, 3)

alumno1 = Alumno(1, "Juan Pérez", "juan@example.com")
alumno2 = Alumno(2, "Ana García", "ana@example.com")

matricula1 = Matricula(1, "2023-01-15", alumno1.id, curso1.id)
matricula2 = Matricula(2, "2023-02-20", alumno2.id, curso1.id)
matricula3 = Matricula(3, "2023-02-25", alumno2.id, curso2.id)

centro_educativo = CentroEducativo()
centro_educativo.realizar_matricula(matricula1.id_matricula, matricula1.fecha_matricula, matricula1.id_alumno, matricula1.id_curso)
centro_educativo.realizar_matricula(matricula2.id_matricula, matricula2.fecha_matricula, matricula2.id_alumno, matricula2.id_curso)
centro_educativo.realizar_matricula(matricula3.id_matricula, matricula3.fecha_matricula, matricula3.id_alumno, matricula3.id_curso)

curso1.mostrar_ficha()
alumno1.mostrar_ficha()

print("Alumno1 se matricula en un curso:")
centro_educativo.mostrar_matriculas([alumno1, alumno2], [curso1, curso2])

print("Alumno2 se matricula en dos cursos:")
centro_educativo.mostrar_matriculas([alumno1, alumno2], [curso1, curso2])
