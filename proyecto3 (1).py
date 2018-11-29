
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import json


def archivojson():
    try:
        with open('Pacientes.json', 'r') as file:
            data = json.load(file)
        file.close()
    except IOError:
        data = []
    return data


def save_file(data):
    print("Save File")

    with open('Pacientes.json', 'w') as file:
        json.dump(data, file, indent=5)
    file.close()


class VentanaInicio():

    def __init__(self):
        print("Constructor")
        self.builder = Gtk.Builder()
        self.builder.add_from_file("Registro3.glade")

        window = self.builder.get_object("VentanaInicio")
        window.connect("destroy", Gtk.main_quit)
        window.set_default_size(600, 400)
        window.set_title("Gestion de horas para Pacientes")

        self.button_open_dialog = self.builder.get_object("IngresarPaciente")
        self.button_open_dialog.connect("clicked", self.agregar)
        
        self.button_buscar = self.builder.get_object("BuscarPaciente")
        self.button_buscar.connect("clicked", self.buscarpaciente)
        
        self.rutpaciente = self.builder.get_object("RutPaciente")
        
        self.button_listap = self.builder.get_object("ListadePacientes")
        self.button_listap.connect("clicked", self.listap)
        

        self.button_search = self.builder.get_object("BuscarPD")
        self.button_search.connect("clicked", self.buscar)

        window.show_all()

    def buscarpaciente (self, btn=None):
        rut = self.rutpaciente.get_text()
        d = VentanaBuscador(rut)
		
    def agregar(self, btn=None):
        print("Aprete el boton add")
        d = DialogoPaciente()
        response = d.dialogo.run()

        if response == Gtk.ResponseType.OK:
            print("Aprete OK")
            
        elif response == Gtk.ResponseType.CANCEL:
            print("Aprete Cancelar")


    def listap(self, btn=None):
      d = MostrarListaPacientes()
               
       
    def buscar(self, bnt=None):
        buscar = BusquedaDoctor()
        
class VentanaBuscador():
	
    def __init__(self, rut):
        print("Constructor")
        self.rut = rut
        self.builder = Gtk.Builder()
        self.builder.add_from_file("Registro3.glade")
        
        self.buscador = self.builder.get_object("Buscador")
        
        self.boton_eliminar = self.builder.get_object("eliminar")
        self.boton_eliminar.connect("clicked", self.eliminar)
         
        self.listmodel = Gtk.ListStore(str, str, str, str, str)
        self.treeResultado = self.builder.get_object("treeResultado1")
        self.treeResultado.set_model(model=self.listmodel)

        cell = Gtk.CellRendererText()
        title = ("Hora", "Nombre", "Rut","Apellido","Doctor")
        for i in range(len(title)):
            col = Gtk.TreeViewColumn(title[i], cell, text=i)
            self.treeResultado.append_column(col)

        self.mostrar()    
        self.buscador.show_all()
        
    
    def eliminar(self, bnt=None):
        data = archivojson()
        for i in range(len(data)):
            if(self.rut == data[i]['rut']):
                it = i
                data.pop(it)
                save_file(data)
		self.mostrar()
		
    def mostrar(self):
		
        data = archivojson()
        for i in range(len(data)):
            if(self.rut == data[i]['rut']):
                busqueda = data[i].values()
                self.listmodel.append(busqueda)
        self.buscador.show_all()
            
class MostrarListaPacientes ():
    def __init__(self):
        print("Constructor")
       
        self.builder = Gtk.Builder()
        self.builder.add_from_file("Registro3.glade")
        self.VentanaPacientes = self.builder.get_object("ListaPacientes")
        self.VentanaPacientes.set_title("Lista de Pacientes")
               
        self.listmodel = Gtk.ListStore(str, str, str, str, str)
        self.treeResultado = self.builder.get_object("treeResultado")
        self.treeResultado.set_model(model=self.listmodel)

        cell = Gtk.CellRendererText()
        title = ("Hora", "Nombre", "Rut","Apellido","Doctor", )
        for i in range(len(title)):
            col = Gtk.TreeViewColumn(title[i], cell, text=i)
            self.treeResultado.append_column(col)

        self.show_all_data()
        self.VentanaPacientes.show_all()
        
    def show_all_data(self):
        data = archivojson()
        for i in data:
            x = [x for x in i.values()]
            self.listmodel.append(x)
               
        
class DialogoPaciente():

    def __init__(self):
        print("Constructor")
        # Creamos un objeto builder para manipular Gtk
        self.builder = Gtk.Builder()
        # Agregamos los objetos Gtk disenados en Glade
        self.builder.add_from_file("Registro3.glade")

        self.dialogo = self.builder.get_object("dialogoPaciente")
        self.dialogo.show_all()

        self.button_cancel = self.builder.get_object("buttonCance")
        self.button_cancel.connect("clicked", self.button_cancel_clicked)

        self.button_ok = self.builder.get_object("buttonOk")
        self.button_ok.connect("clicked", self.button_ok_clicked)

        
        self.hora = self.builder.get_object("entryHora")
        self.nombre = self.builder.get_object("entryNombre")
        self.rut = self.builder.get_object("entryRut")
        self.apellido = self.builder.get_object("entryApellido")
        self.doctor = self.builder.get_object("entryDoctor")
       

    def button_ok_clicked(self, btn=None):
       
        hora = self.hora.get_text()
        nombre = self.nombre.get_text()
        rut = self.rut.get_text()
        apellido = self.apellido.get_text()
        doctor = self.doctor.get_text()
        

        j = {"hora": hora,
            "nombre": nombre,
            "rut": rut, 
            "apellido": apellido, 
            "doctor": doctor
            }
            
        f = archivojson()
        f.append(j)
        save_file(f)
     
        self.dialogo.destroy()

    def button_cancel_clicked(self, btn=None):
        self.dialogo.destroy()

class BusquedaDoctor():

    def __init__(self):
        print("Constructor")
        # Creamos un objeto builder para manipular Gtk
        self.builder = Gtk.Builder()
        # Agregamos los objetos Gtk disenados en Glade
        self.builder.add_from_file("Registro3.glade")

        self.dialogo = self.builder.get_object("BusquedaD")
        self.dialogo.show_all()

        self.button_cancel = self.builder.get_object("entryCancelar")
        self.button_cancel.connect("clicked", self.button_cancel_clicked)
        
        self.button_buscar = self.builder.get_object("BuscarDoctor")
        self.button_buscar.connect("clicked", self.button_busqueda)
        
        self.button_ok = self.builder.get_object("entryAceptar")
        self.button_ok.connect("clicked", self.button_ok_clicked)

        self.busqueda = self.builder.get_object("busqueda")
        self.label_datos = self.builder.get_object("datos")
        
    def button_busqueda(self, btn=None):
        busqueda = self.busqueda.get_text()
        f = archivojson()
        for i in range(len(f)):
            if busqueda == f[i]["doctor"]:
                paciente = "Paciente: " + f[i]["nombre"]
                self.label_datos.set_text(paciente)
				
        print(texto)
	  
    def button_ok_clicked(self, btn=None):
        self.dialogo.destroy()

    def button_cancel_clicked(self, btn=None):
        self.dialogo.destroy()

		
if __name__ == "__main__":
    p = VentanaInicio()
    Gtk.main()
