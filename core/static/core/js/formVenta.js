$().ready(function() {
    $.validator.addMethod("formrut", function (value, element) {
        var patron = resultado(value)
        return this.optional(element) || patron;
     }, "Formato del rut incorrecto");
     $.validator.addMethod("formtarjeta", function (value, element) {
        var patron = /^(?:(4[0-9]{12}(?:[0-9]{3})?)|(5[1-5][0-9]{14})|(6(?:011|5[0-9]{2})[0-9]{12})|(3[47][0-9]{13})|(3(?:0[0-5]|[68][0-9])[0-9]{11})|((?:2131|1800|35[0-9]{3})[0-9]{11}))$/;
        return this.optional(element) || patron.test(value);
     }, "Formato del tarjeta incorrecto");
    // validate the comment form when it is submitted
    $("#registration").validate({
        rules: {
            producto: {
                required: true
            },
            cantidad:{
                required: true
            },
            rut: {
                required: true,
                formrut: true
            },
            email: {
                required: true,
                email: true
            },
            metodo: {
                required: true
            },
            tarjeta: {
                required: true,
                formtarjeta: true,
                minlength:16
            },
            fecha: {
                required: true
            },
            cvv: {
                required: true,
                minlength:3,
                maxlength:3
            },
            direccion: {
                required: true,
                minlength: 15
            },

        },
        messages: {
            producto: {
                required: "Debes seleccionar un producto"
            },
            cantidad: {
                required: "Debes seleccionar una cantidad del producto a comprar",
            },
            email: {
                required: "Debes ingresar un email válido",
                email: "Email ingresado no es válido"
            },
            rut: {
                required: "Debe ingresar su rut",
                formrut: "Rut ingresado no válido"
            },
            metodo: {
                required: "Debes seleccionar un metodo de pago"
            },
            tarjeta: {
                formtarjeta: "Debes ingresar el numero de tu tarjeta valido",
                required: "Debes ingresar el numero de tu tarjeta valido",
                minlength: "Faltan digitos de su tarjeta"
            },
            cvv: {
                required: "Debes ingresar los 3 digitos de la parte trasera de tu tarjeta",
                minlength: "Faltan digitos de su CVV",
                maxlength: "Sobrepasaste la cantidad de digitos de tu CVV"
            },
            fecha: {
                required: "Debes ingresar la fecha de expiración"
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