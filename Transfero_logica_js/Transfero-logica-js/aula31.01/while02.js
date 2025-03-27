let nome , cadastro = "";
let continua = "s";
let i = 0;
while (continua == "s"){
    nome = prompt("Olá bem vindo a Casas Bahia!\n Para se cadastrar insira seu nome por favor no campo abaixo:");
    cadastro = cadastro + nome + "<br>";
    i++;
    continua = prompt("Deseja continuar?<s/>n>");
}
document.writeln(cadastro);
document.writeln("Foram lidos" + i + "nomes");