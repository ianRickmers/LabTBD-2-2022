from faker import Faker
import random as rd

# objeto faker global
fake = Faker('es_CL')

def FakerCliente(n):
    i = 1
    f = 0
    pk = []
    genero = ['F','M']
    while(i<=n):
        string = ''
        rut = str(rd.randint(10000000,99999999))
        while rut in pk:
            rut = str(rd.randint(10000000,99999999))
        pk.append(rut)
        if (i==n):
            string = '('
            string = string + rut + ', '
            string = string + str(rd.randint(0,9)) + ', '
            string = string + '\'' + fake.first_name() + '\'' + ', '
            string = string + '\'' + fake.last_name() + '\'' + ', '
            string = string + '\'' + str(rd.choice(genero)) + '\'' + ', '
            string = string + str(rd.randint(1,32)) + ');'
            print(string)
            i = i + 1
            return pk
        if(f == 0):
            print('INSERT INTO public.cliente(')
            print('rut, dv, nombre, apellido, genero, "idComuna")')
            string = 'VALUES ('
            string = string + rut + ', '
            string = string + str(rd.randint(0,9)) + ', '
            string = string + '\'' + fake.first_name() + '\'' + ', '
            string = string + '\'' + fake.last_name() + '\'' + ', '
            string = string + '\'' + str(rd.choice(genero)) + '\'' + ', '
            string = string + str(rd.randint(1,32)) + '),'
            print(string)
            f = f + 1
            i = i + 1
        
        else:
            string = '('
            string = string + rut + ', '
            string = string + str(rd.randint(0,9)) + ', '
            string = string + '\'' + fake.first_name() + '\'' + ', '
            string = string + '\'' + fake.last_name() + '\'' + ', '
            string = string + '\'' + str(rd.choice(genero)) + '\'' + ', '
            string = string + str(rd.randint(1,32)) + '),'
            print(string)
            i = i + 1
    




def FakerCliente_Pelu(n,pk):
    i = 1
    f = 0
    while(i<=n):
        string = ''
        if (i==n):
            string = '('
            string = string + rd.choice(pk) + ', '
            string = string + str(rd.randint(1,25)) + ', '
            string = string + str(i) + '); '
            print(string)
            i = i + 1
            return 
        if(f == 0):
            print('INSERT INTO public.cliente_pelu(')
            print('"idCliente", "idPeluqueria", "idCita")')
            string = 'VALUES ('
            string = string + rd.choice(pk) + ', '
            string = string + str(rd.randint(1,25)) + ', '
            string = string + str(i) + '), '
            print(string)
            i = i + 1
            f = f + 1
        
        else:
            string = '('
            string = string + rd.choice(pk) + ', '
            string = string + str(rd.randint(1,25)) + ', '
            string = string + str(i) + '), '
            print(string)
            i = i + 1
    




def FakerPeluqueria(n):
    i = 1
    f = 0
    while(i<=n):
        string = ''
        if (i==n):
            string = '('
            string = string + str(i) + ', '
            string = string + '\'' + 'Peluqueria ' + fake.first_name() + '\'' + ', '
            string = string + '\'' + fake.street_name() + '\'' + ', '
            string = string + fake.building_number() + ', '
            string = string + str(rd.randint(1,32)) + ');'
            print(string)
            i = i + 1
            return
        if(f == 0):
            print('INSERT INTO public.peluqueria(')
            print('id, nombre, direccion, numero, "idComuna")')
            string = 'VALUES ('
            string = string + str(i) + ', '
            string = string + '\'' + 'Peluqueria ' + fake.first_name() + '\'' + ', '
            string = string + '\'' + fake.street_name() + '\'' + ', '
            string = string + fake.building_number() + ', '
            string = string + str(rd.randint(1,32)) + '),'
            print(string)
            i = i + 1
            f = f + 1
        
        else:
            string = '('
            string = string + str(i) + ', '
            string = string + '\'' + 'Peluqueria ' + fake.first_name() + '\'' + ', '
            string = string + '\'' + fake.street_name() + '\'' + ', '
            string = string + fake.building_number() + ', '
            string = string + str(rd.randint(1,32)) + '),'
            print(string)
            i = i + 1
    return 


            
def FakerEmpleado(n,pk):
    i = 1
    f = 0
    ek = []
    while(i<=n):
        string = ''
        rut = str(rd.randint(10000000,99999999))
        while rut in pk or rut in ek :
            rut = str(rd.randint(10000000,99999999))
        ek.append(rut)
        if (i==n):
            string = '('
            string = string + rut + ', '
            string = string + str(rd.randint(0,9)) + ', '
            string = string + '\'' + fake.first_name() + '\'' + ', '
            string = string + '\'' + fake.last_name() + '\'' + ', '
            string = string + str(rd.randint(1,32)) + ', '
            string = string + str(rd.randint(1,25)) + ');'
            print(string)
            i = i + 1
            return ek
        if(f == 0):
            print('INSERT INTO public.empleado(')
            print('rut, dv, nombre, apellido, "idComuna", "idPeluqueria")')
            string = 'VALUES ('
            string = string + rut + ', '
            string = string + str(rd.randint(0,9)) + ', '
            string = string + '\'' + fake.first_name() + '\'' + ', '
            string = string + '\'' + fake.last_name() + '\'' + ', '
            string = string + str(rd.randint(1,32)) + ', '
            string = string + str(rd.randint(1,25)) + '),'
            print(string)
            f = f + 1
            i = i + 1
        
        else:
            string = '('
            string = string + rut + ', '
            string = string + str(rd.randint(0,9)) + ', '
            string = string + '\'' + fake.first_name() + '\'' + ', '
            string = string + '\'' + fake.last_name() + '\'' + ', '
            string = string + str(rd.randint(1,32)) + ', '
            string = string + str(rd.randint(1,25)) + '),'
            print(string)
            i = i + 1         
    return ek 

# no puede ser mayor a la cantidad de empleados
def FakerPeluquero(n,pk):
    i = 1
    f = 0
    ruts = pk.copy()
    while(i<=n):
        string = ''
        rut = ruts.pop(rd.randint(0,len(ruts)-1))
        if (i==n):
            string = '('
            string = string + str(i) + ', '
            string = string + rut + ');'
            print(string)
            i = i + 1
            return 
        if(f == 0):
            print('INSERT INTO public.peluquero(')
            print('id, "idEmpleado")')
            string = 'VALUES ('
            string = string + str(i) + ', '
            string = string + rut + '),'
            print(string)
            i = i + 1
            f = f + 1
        
        else:
            string = '('
            string = string + str(i) + ', '
            string = string + rut + '),'
            print(string)
            i = i + 1
    return 


def FakerCita(n,p):
    i = 1
    f = 0
    year = 2017
    while(i<=n):
        string = ''
        
        if(i== n//6 ) or (i == (2*n//6) ) or (i==3*n//6 ) or (i==4*n//6 ) or (i==5*n//6 )or (i==6*n//6 ):
            year = year + 1
        if (i==n):
            string = '('
            string = string + str(i) + ', '
            string = string + str(rd.randint(1,5)) + ', '
            string = string + str(rd.randint(1,3)) + ', '
            string = string + str(year) + ', '
            string = string + str(i) + ', '
            string = string + str(rd.randint(1,p)) + ', '
            string = string + str(rd.randint(1,9)) + ');'
            print(string)
            i = i + 1
            return     
        if(f == 0):
            print('INSERT INTO public.cita(')
            print('id, dia, mes, "ano", "idDetalle", "idPeluquero", "idHorario")')
            string = 'VALUES ('
            string = string + str(i) + ', '
            string = string + str(rd.randint(1,5)) + ', '
            string = string + str(rd.randint(1,3)) + ', '
            string = string + str(year) + ', '
            string = string + str(i) + ', '
            string = string + str(rd.randint(1,p)) + ', '
            string = string + str(rd.randint(1,9)) + '),'
            print(string)
            i = i + 1
            f = f + 1
        
        else:
            string = '('
            string = string + str(i) + ', '
            string = string + str(rd.randint(1,5)) + ', '
            string = string + str(rd.randint(1,3)) + ', '
            string = string + str(year) + ', '
            string = string + str(i) + ', '
            string = string + str(rd.randint(1,p)) + ', '
            string = string + str(rd.randint(1,9)) + '),'
            print(string)
            i = i + 1
    return 

def FakerDetalle(n):
    i = 1
    f = 0
    while(i<=n):
        string = ''
        if (i==n):
            string = '('
            string = string + str(i) + ', '
            string = string + str(rd.randint(1,120)) + ', '
            string = string + str(i) + ');'
            print(string)
            i = i + 1
            return 
        if(f == 0):
            print('INSERT INTO public.detalle(')
            print('id, duracion, "idPago")')
            string = 'VALUES ('
            string = string + str(i) + ', '
            string = string + str(rd.randint(1,120)) + ', '
            string = string + str(i) + '),'
            print(string)
            i = i + 1
            f = f + 1
        
        else:
            string = '('
            string = string + str(i) + ', '
            string = string + str(rd.randint(1,120)) + ', '
            string = string + str(i) + '),'
            print(string)
            i = i + 1
    return 

def FakerPago(n):
    i = 1
    f = 0
    while(i<=n):
        string = ''
        if (i==n):
            string = '('
            string = string + str(i) + ', '
            string = string + str(rd.randrange(5000,80000,2500)) + '); '
            print(string)
            i = i + 1
            return 
        if(f == 0):
            print('INSERT INTO public.pago(')
            print('id, total)')
            string = 'VALUES ('
            string = string + str(i) + ', '
            string = string + str(rd.randrange(5000,80000,2500)) + '), '
            print(string)
            i = i + 1
            f = f + 1
        
        else:
            string = '('
            string = string + str(i) + ', '
            string = string + str(rd.randrange(5000,80000,2500)) + '), '
            print(string)
            i = i + 1
    return 

def FakerSueldo(pk):
    i = 0
    f = 0
    ID = 1

    ruts = pk.copy()
    n = len(ruts)

    year = 2020
    mes = 1
    
    while(True):
        
        string = ''

        if(i == n):
            i = 0
            mes = mes + 1
            
        if(mes == 13):
            mes = 1
            year = year + 1

        if(ID == n*36):
            string = '('
            string = string + str(ID) + ', '
            string = string + str(rd.randrange(350000,550000,50000)) + ', '
            string = string + str(rd.randint(29,30)) + ', '
            string = string + str(mes) + ', '
            string = string + str(year) + ', '
            string = string + ruts[i] + ');'
            print(string)
            i = i + 1
            ID = ID + 1
            return
        if(f == 0):
            print('INSERT INTO public.sueldo(')
            print('id, monto, dia, mes, "ano", "idEmpleado")')
            string = 'VALUES ('
            string = string + str(ID) + ', '
            string = string + str(rd.randrange(350000,550000,50000)) + ', '
            string = string + str(rd.randint(29,30)) + ', '
            string = string + str(mes) + ', '
            string = string + str(year) + ', '
            string = string + ruts[i] + '),'
            print(string)
            i = i + 1
            ID = ID + 1
            f = f + 1
        
        else:
            string = '('
            string = string + str(ID) + ', '
            string = string + str(rd.randrange(350000,550000,50000)) + ', '
            string = string + str(rd.randint(29,30)) + ', '
            string = string + str(mes) + ', '
            string = string + str(year) + ', '
            string = string + ruts[i] + '),'
            print(string)
            i = i + 1
            ID = ID + 1
    return

def FakerProductoDetalle(n):
    i = 1
    f = 0
    c = 0
    while(i<=n):
        string = ''
        if (i==n and c==3):
            string = '('
            string = string + str(rd.randrange(1,5,1)) + ', '
            string = string + str(i) + '); '
            print(string)
            return 
            if c<3:
                c = c + 1
            else:
                i = i + 1
                c = 1
        if(f == 0):
            print('INSERT INTO public.producto_detalle(')
            print('"idProducto", "idDetalle")')
            string = 'VALUES ('
            string = string + str(rd.randrange(1,5,1)) + ', '
            string = string + str(i) + '), '
            print(string)
            c = c + 1
            f = f + 1
        
        else:
            string = '('
            string = string + str(rd.randrange(1,5,1)) + ', '
            string = string + str(i) + '), '
            print(string)
            if c<3:
                c = c + 1
            else:
                i = i + 1
                c = 1
    return

def FakerServicioDetalle(n):
    i = 1
    f = 0
    c = 0
    while(i<=n):
        string = ''
        if (i==n and c==3):
            string = '('
            string = string + str(rd.randrange(1,5,1)) + ', '
            string = string + str(i) + '); '
            print(string)
            return 
            if c<3:
                c = c + 1
            else:
                i = i + 1
                c = 0
        if(f == 0):
            print('INSERT INTO public.servicio_detalle(')
            print('"idServicio", "idDetalle")')
            string = 'VALUES ('
            string = string + str(rd.randrange(1,5,1)) + ', '
            string = string + str(i) + '), '
            print(string)
            c = c + 1
            f = f + 1
        
        else:
            string = '('
            string = string + str(rd.randrange(1,5,1)) + ', '
            string = string + str(i) + '), '
            print(string)
            if c<3:
                c = c + 1
            else:
                i = i + 1
                c = 0
    return

def FakerPrecio():
    i = 1
    f = 0
    monto = 2000
    while(i<=15):
        string = ''
        if (i==15):
            string = '('
            string = string + str(i) + ', '
            string = string + str(monto) + '); '
            print(string)
            i = i + 1
            monto = monto + 500
            return 
        if(f == 0):
            print('INSERT INTO public.precio(')
            print('id, monto)')
            string = 'VALUES ('
            string = string + str(i) + ', '
            string = string + str(monto) + '), '
            print(string)
            monto = monto + 500
            i = i + 1
            f = f + 1
        
        else:
            string = '('
            string = string + str(i) + ', '
            string = string + str(monto) + '), '
            print(string)
            i = i + 1
            monto = monto + 500
    return 

def FakerPrecioServicio():
    i = 1
    f = 0
    ID = 1
    while(True):
        
        if(i == 6):
            ID = ID + 1
            i = 1

        if(ID == 26):
            return
        
        string = ''
        if (ID == 25) and (i==5):
            string = '('
            string = string + str(rd.randint(1,15)) + ', '
            string = string + str(i) + ', '
            string = string + str(ID) + '); '
            print(string)
            i = i + 1
            return 
        if(f == 0):
            print('INSERT INTO public.servicio_precio(')
            print('"idPrecio", "idServicio", "idPeluqueria")')
            string = 'VALUES ('
            string = string + str(rd.randint(1,15)) + ', '
            string = string + str(i) + ', '
            string = string + str(ID) + '), '
            print(string)
            i = i + 1
            f = f + 1
        
        else:
            string = '('
            string = string + str(rd.randint(1,15)) + ', '
            string = string + str(i) + ', '
            string = string + str(ID) + '), '
            print(string)
            i = i + 1
    return
#LLamados variables
clientes=int(input("Cantidad Clientes: "))
empleados=int(input("Cantidad empleados: "))
citas=int(input("Cantidad citas: "))
print('\n')
print(';')
f = open("db.txt","r",encoding='utf-8')
print(f.read())
print('\n\n')
f = open("comunas.txt","r",encoding='utf-8')
print(f.read())
print('\n\n')
listaClientes=FakerCliente(clientes)
print('\n\n')
listaPeluquerias=FakerPeluqueria(25)
print('\n\n')
listaEmpleados=FakerEmpleado(empleados,listaClientes)
print('\n\n')
FakerSueldo(listaEmpleados)
print('\n\n')
FakerPeluquero(empleados,listaEmpleados)
print('\n\n')
f = open("horarios.txt","r",encoding='utf-8')
print(f.read())
print('\n\n')
FakerPago(citas)
print('\n\n')
FakerDetalle(citas)
print('\n\n')
FakerCita(citas,empleados)
print('\n\n')
FakerCliente_Pelu(citas,listaClientes)
print('\n\n')
f = open("ultimo.txt","r",encoding='utf-8')
print(f.read())
print('\n\n')
FakerProductoDetalle(citas)
print('\n\n')
FakerServicioDetalle(citas)
print('\n\n')
FakerPrecio()
print('\n\n')
FakerPrecioServicio()
print('\n\n')


