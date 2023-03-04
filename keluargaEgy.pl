%AI2023B-Tugas03-EgyVedriyanto-2117051035

%Fakta-Fakta :
%Saya Egy.
%Kakek saya Iskandar.
%Ayah saya Didi, dan Paman saya dodi.
%Saudara kandung saya Qia dan Kirana.
%Anak paman saya yaitu Discha dan Langit.

kakek(iskandar, egy).
kakek(iskandar, discha).

ayah(iskandar, didi).
ayah(iskandar, dodi).

ayah(didi, egy).
ayah(didi, qia).
ayah(didi, kirana).

anak(discha, dodi).
anak(langit, dodi).

saudara_kandung(qia, kirana).
saudara_kandung(kirana, qia).
saudara_kandung(qia, egy).
saudara_kandung(kirana, egy).
saudara_kandung(egy, qia).
saudara_kandung(egy, kirana).

saudara_kandung(discha, langit).
saudara_kandung(langit, discha).

%Rules Anak
anak(X, Y) :- ayah(Y, X) ; saudara_kandung(X, Z) , ayah(Y, Z) , X \= Z.

%Rules Ayah
ayah(X, Y) :- anak(Y, X) ; saudara_kandung(Y, Z) , ayah(X, Z) , Y \= Z.

%Rules Saudara Kandung
saudara_kandung(X, Y) :- ayah(Z, X) , ayah(Z, Y) , X \= Y.

%Rules Paman
paman(X, Y) :- ayah(Z, Y) , saudara_kandung(X, Z).

%Rules Sepupu
sepupu(X, Y) :- ayah(Z, X), ayah(W, Y), saudara_kandung(Z, W), X \= Y.

%Rules Kakek
kakek(X, Y) :- ayah(X, Z), ayah(Z, Y).
kakek(X, Y) :- ayah(X, Z), anak(Y, Z).
kakek(X, Y) :- kakek(X, Z), saudara_kandung(Y, Z)

%Rules Keturunan
keturunan(X, Y) :- ayah(Y, X).
keturunan(X, Y) :- anak(X, Y).
keturunan(X, Y) :- ayah(Z, X), ayah(Y, Z).
keturunan(A, B) :- kakek(B, A).