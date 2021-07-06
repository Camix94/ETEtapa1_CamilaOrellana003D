document.addEventListener("DOMContentLoaded", function(event) {
    document.getElementById('form_1').addEventListener('submit', 
  manejadorValidacion)
  });
  
  function manejadorValidacion(e) {
    e.preventDefault();
    var msg = document.getElementById('msg');
    msg.innerText = '';

    if(this.querySelector('[name=nombre]').value == '') {
    console.log('El nombre está vacío');
    msg.innerText = 'Debes escribir un nombre';
    return;
    }

    if(! validateNombre(this.querySelector('[name=nombre]').value)) 
        { console.log('El nombre no es válido');
        msg.innerText = 'Debes escribir un nombre válido'; 
        return;
    }

    if(! validatePais(this.querySelector('[name=pais]').value)) 
        { console.log('El nombre del país no es válido');
        msg.innerText = 'Debes escribir un país válido'; 
        return;
    }

    if(this.querySelector('[name=email]').value == '') {
        console.log('El email está vacío');
        msg.innerText = 'Debes escribir un correo';
        return;
        }

    if(! validateEmail(this.querySelector('[name=email]').value)) 
        { console.log('El email no es válido');
        msg.innerText = 'Debes escribir un email válido'; 
        return;
    }

    if(this.querySelector('[name=fono]').value == '') {
        console.log('El teléfono está vacío');
        msg.innerText = 'Debes escribir un número de teléfono';
        return;
        }

    if(! validateFono(this.querySelector('[name=fono]').value)) 
        { console.log('El número ingresado no es válido');
        msg.innerText = 'Debes ingresar un número de teléfono valido de minímo 9 dígitos y máximo 14'; 
        return;
    }
    

    if(this.querySelector('[name=nroIdentificacion]').value == '') {
        console.log('El rut está vacío');
        msg.innerText = 'Debes escribir un número de identificación';
        return;
        }

    if(! validateIde(this.querySelector('[name=nroIdentificacion]').value)) 
        { console.log('El rut no es válido');
        msg.innerText = 'Debes escribir un número de identificación válido. Si termina en letra, reemplácelo por 0'; 
        return;
    }

    this.submit();
  }
  
  function validateEmail(email) {
    var re = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
    return re.test((email).toLowerCase());
   }

   function validateNombre(nombre) {
    var nom = /^[a-zA-ZÀ-ÿ\s]{3,500}$/;
    return nom.test((nombre));
   }

   function validatePais(pais) {
    var nom = /^[a-zA-ZÀ-ÿ\s]{3,200}$/;
    return nom.test((pais));
   }

   function validateFono(fono) {
    var fo = /^\d{9,14}$/;
    return fo.test((fono));
   }

   function validateIde(nroIdentificacion) {
    var ide = /^\d{8,20}$/;
    return ide.test((nroIdentificacion));
   }

   