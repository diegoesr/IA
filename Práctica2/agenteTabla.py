ACCIONES={'ST':'Cerrado, ingrese una tarjeta valida o recargue',
          'ST,TCS':'Pase',
          'ST,TCS,TSS':'Saldo insuficiente',
          'ST,TSS':'Saldo insuficiente',
          'ST,TSS,TCS':'PASE',
          'ST,TSS,ST,TSS':'Saldo insuficiente',
}

class AgenteTabla:

    def __init__(self,acciones):
        self.acciones=acciones
        self.percepciones=""

    def actuar(self,percepcion,accion_basica=''):
        if not percepcion:
            return accion_basica
        if len(self.percepciones)!=0:
            self.percepciones+=','
        self.percepciones+=percepcion
        if self.percepciones in self.acciones.keys():
            return self.acciones[self.percepciones]
        self.percepciones=''
        return accion_basica
    
torniquete=AgenteTabla(ACCIONES)
percepcion=input("Leyendo tarjeta ...... verificando.")
while percepcion:
    accion=torniquete.actuar(percepcion, 'Cerrado')
    print(accion)
    percepcion=input("Lee la tarjeta: ")

    