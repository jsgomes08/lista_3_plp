% Fatos para tipos sanguíneos
tiposanguineo(joao, a).
tiposanguineo(davi, a).
tiposanguineo(maria, a).
tiposanguineo(ana, a).
tiposanguineo(julia, o).
tiposanguineo(alice, a).
tiposanguineo(pedro, a).
tiposanguineo(laura, b).
tiposanguineo(manuela, b).
tiposanguineo(vitoria, b).
tiposanguineo(manuel, o).
tiposanguineo(jose, ab).
tiposanguineo(carlos, ab).
tiposanguineo(telma, o).

% Fatos para fator RH
fatorrh(joao, +).
fatorrh(davi, +).
fatorrh(maria, -).
fatorrh(ana, -).
fatorrh(julia, +).
fatorrh(alice, +).
fatorrh(pedro, -).
fatorrh(laura, +).
fatorrh(manuela, -).
fatorrh(vitoria, +).
fatorrh(manuel, +).
fatorrh(jose, +).
fatorrh(carlos, -).
fatorrh(telma, -).

% Fatos para peso
peso(joao, 75.7).
peso(davi, 50).
peso(maria, 49).
peso(ana, 80).
peso(julia, 47).
peso(alice, 30).
peso(pedro, 20).
peso(laura, 54).
peso(manuela, 61).
peso(vitoria, 70).
peso(manuel, 130).
peso(jose, 65).
peso(carlos, 48).
peso(telma, 79).

% Fatos para idade
idade(joao, 41).
idade(davi, 24).
idade(maria, 51).
idade(ana, 17).
idade(julia, 15).
idade(alice, 56).
idade(pedro, 10).
idade(laura, 18).
idade(manuela, 66).
idade(vitoria, 12).
idade(manuel, 56).
idade(jose, 100).
idade(carlos, 67).
idade(telma, 48).

% Compatibilidade de tipos sanguíneos
compativel(a, a).
compativel(a, ab).
compativel(b, b).
compativel(b, ab).
compativel(ab, ab).
compativel(o, a).
compativel(o, b).
compativel(o, ab).
compativel(o, o).

% Compatibilidade de fator RH
rhcomp(+, +).
rhcomp(-, +).
rhcomp(-, -).

% Regra principal para determinar aptidão para doação
podedoar(Doador, Receptor) :-
    tiposanguineo(Doador, TipoDoador),
    tiposanguineo(Receptor, TipoReceptor),
    compativel(TipoDoador, TipoReceptor),
    fatorrh(Doador, RhDoador),
    fatorrh(Receptor, RhReceptor),
    rhcomp(RhDoador, RhReceptor),
    idade(Doador, Idade),
    Idade >= 18, Idade =< 65,
    peso(Doador, Peso),
    Peso > 50.
