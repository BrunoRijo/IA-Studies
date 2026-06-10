unit SistemaExemplo;
// Arquivo ficticio criado somente para os exercicios.

uses
  SysUtils;

var
  Nome: string;
  Idade: Integer;
  Salario: Double;

//TODO function ProcessaDados
//TODO procedure VerificaInformacoes

procedure LerDados;
begin
  Write('Digite seu nome: ');
  ReadLn(Nome);

  Write('Digite sua idade: ');
  ReadLn(Idade);
end;

function CalcularBonus(SalarioBase: Double): Double;
begin
  Result := SalarioBase * 0.10;
end;

procedure ExibirDados;
begin
  WriteLn('Nome: ', Nome);
  WriteLn('Idade: ', Idade);
end;

procedure ExportarDados;
begin
  WriteLn('Exportando...');
end;

begin
  WriteLn('Iniciando sistema...');

  LerDados;

  Salario := 3500.00;

  ExibirDados;

  WriteLn('Bônus: ', CalcularBonus(Salario):0:2);

  ExportarDados;

  WriteLn('Finalizando sistema...');
  ReadLn;
end.