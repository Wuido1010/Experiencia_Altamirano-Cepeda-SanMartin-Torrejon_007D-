$().ready(function() {
    $.validator.addMethod("formrut", function (value, element) {
        var patron = resultado(value)
        return this.optional(element) || patron;
     }, "Formato del rut incorrecto");
    // validate the comment form when it is submitted
    $("#formulario").validate({
        rules: {
            nombre: {
                required: true,
                minlength: 2
            },
            apellido:{
                required: true,
                minlength: 2
            },
            rut: {
                required: true,
                formrut: true
            },
            email: {
                required: true,
                email: true
            },
            contraseña: {
                required: true,
                minlength: 7
            },
            conficontraseña: {
                required: true,
                equalTo: "#contraseña"
            },
            genero: {
                required: true
            },
            suscripcion: {
                required: true
            },
            direccion: {
                required: true,
                minlength: 8
            },

        },
        messages: {
            nombre: {
                required: "Debes ingresar tus nombres",
                minlength: "Debes ingresar al menos 2 caracteres"
            },
            apellido: {
                required: "Debes ingresar tus apellidos",
                minlength: "Debes ingresar al menos 2 caracteres"
            },
            email: {
                required: "Debes ingresar un email válido",
                email: "Email ingresado no es válido"
            },
            rut: {
                required: "Debe ingresar su rut",
                formrut: "Rut ingresado no válido"
            },
            contraseña: {
                required: "Debes una contraseña",
                minlength: "La contraseña debe tener al menos 7 caracteres"
            },
            conficontraseña: {
                required: "Debes ingresar tu contraseña nuevamente",
                equalTo: "Las contraseñas no coinciden"
            },
            genero: {
                required: "Debes seleccionar un género"
            },
            suscripcion: {
                required: "Debes seleccionar si desea suscribirse o no"
            },
            direccion: {
                required: "Debes ingresar tu dirección",
                minlength: "Tu dirección debe tener al menos 15 caracteres"
            }


        }

    });
});
//funcion para que seleccione solo 1 checkbox
function getSelectItemThat(id) {
    for (var i = 1;i <= 4; i++)
    {
        document.getElementById(i).checked = false;
    }
    document.getElementById(id).checked = true;
}

//funcion para validar el rut
class RutValidador {
    constructor(rut) {
        this.rut = rut;
        //Obtendremos el ultimo caracter del rut
        this.dv = rut.substring(this.rut.length - 1);
        //Limpiar el rut dejando solamente los numeros
        this.rut = this.rut.substring(0, this.rut.length -1).replace(/\D/g,'');
        this.esValido = this.validar()
    }

    validar(){
        let numerosArray = this.rut.split('').reverse()
        let acomulador = 0;
        let multiplicador = 2;
        for (let numero of numerosArray) {
            acomulador += parseInt(numero) * multiplicador;
            multiplicador++;

            if (multiplicador == 8){
                multiplicador = 2;
            }
        }

        let dv = 11 - (acomulador%11);
        if(dv == 11){
            dv = '0';
        }
        if(dv == 10){
            dv = 'k';
        }
        return dv == this.dv.toLowerCase();
    }

    formato(){
        if(!this.esValido) return '';

        return (this.rut.toString().replace(/\B(?=(\d{3})+(?!\d))/g,'.'))+'-'+this.dv;
    }
}

let validador = new RutValidador('30.686.957-4')
console.log(validador.formato())

function resultado(value) {
    let rutValidador = new RutValidador(value)
    if(rutValidador.esValido) {
        return true
    }
    return false
}







