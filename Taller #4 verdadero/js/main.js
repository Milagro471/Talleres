/************************************************validar los campos del login*********************************************************************************************************/
/*************************lectura de los datos**************************/
var btn = document.getElementById("Iniciar Sesión");
Usuario = document.getElementById("Usuario").value;
Contraseña = document.getElementById("Contraseña").value;

btn.addEventListener("click", function(evt) {

    if (Contraseña.value == "") {
        alert("El campo contraseña es obligatorio")
        evt.preventDefault();
        return false;
    } else if (Usuario.value == "") {
        alert("El campo Usuario es obligatorio")
        evt.preventDefault();
        return false;
    } else if (Usuario.value.length > 30) {
        alert.log("El nombre de Usuario es demasiado largo")
        evt.preventDefault();
        return false;
    }
});



/**********************************************************validacion de registrarse************************************************************************/

/*********************************************lectura de datos**************/

var Nombre, Apellido, Usuario, Correo, Contraseña;

var mi_json_en_string = '{"Nombre:"' + Nom + ',"Apellido:"' + Ape + '", "Usuario: "' + Usuario1 + ', "Correo:" ' + Correo1 + '", "Contraseña:"' + Contra1 + '}'

var data_quemada = JSON.parse(mi_json_en_string);

alert(mi_json_en_string[0].Nombre);

alert(mi_json_en_string[0].Apellido);

alert(mi_json_en_string[1].Usuario);

alert(mi_json_en_string[1].Correo);

alert(mi_json_en_string[2].Contraseña);


/*********************************************despleglar los datos****************/

var btn = document.getElementById("Registrar");

var btn = document.getElementById("Registrar").innerHTML = obj_json.Nombre + " ," + obj_json.Apellido + " ," + obj_json.Usuario + " ," + obj_json.Correo + " ," + obj_json.Contraseña + " ,";





/************************************************************validacion de jugadores***********************************************************************/
var Nombre, Apellido, Usuario, Correo, Contraseña;

var mi_json_en_string = '{"Nombre:"' + Nombre + ',"Apellido:"' + Apellido + '", "Usuario: "' + User + ', "Correo:" ' + Correo + '", "Contraseña:"' + Contra + '}'

var doc = JSON.parse(mi_json_en_string);

alert(mi_json_en_string[0].Nombre);

alert(mi_json_en_string[0].Apellido);

alert(mi_json_en_string[1].Usuario);

alert(mi_json_en_string[1].Correo);

alert(mi_json_en_string[2].Contraseña);



var btn = document.getElementById("Jugador Registrado");

var btn = document.getElementById("Jugador Registrado").innerHTML = obj_json.Nombre + " ," + obj_json.Apellido + " ," + obj_json.Usuario + " ," + obj_json.Correo + " ," + obj_json.Contraseña + " ,";



/************************************************boton cerrar************************************************************************************/

function Cerrar() {
    window.close()
}


/**************************************************olvidaste tu contraseña***********************************************************************/

var btn = document.getElementById("Enviar Contraseña");

recuperacion = document.getElementById("recuperacioncontraseña").value;

btn.addEventListener("click", function(evt) {
    if (Contraseña.value == "") {
        alert("El campo contraseña es obligatorio")
        evt.preventDefault();
        return false;
    } else if (Usuario.value == "") {
        alert("El campo Usuario es obligatorio")
        evt.preventDefault();
        return false;

    }
});