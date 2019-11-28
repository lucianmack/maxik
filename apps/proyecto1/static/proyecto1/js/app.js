$(document).ready(function() {
    $("#formulario").validate( {
        errorClass: 'is-invalid',
        rules: {
            nombre:{
                required:true
            },
            correo:{
                required:true,
                email:true
            },
            fnacimiento:{
                required:true
            }
        },
        messages: {
            nombre:{
                required:"Debe ingresar el Nombre"
            },
            correo:{
                required:"Debe ingresar un Email",
                email:"Debe ingresar un correo valido"
            },
            fnacimiento:{
                required:"Ingrese su Fecha de Nacimiento"
            }
        }
    }) 
})



//Mensaje de Alerta Customed
$("#formulario").submit(function() {
    if($("#formulario").valid()) {
        return true;
    } else{
        Swal.fire({
            type: 'error',
            title: 'Oops...',
            text: 'Lo sentimos, pero debes llenar todos los campos obligatorios',
            footer: '<a href>Why do I have this issue?</a>'
          })
    }
    return false
})