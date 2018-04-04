f = [1 1]; %nbPanneaux + nb Eolienne

%Ouverture du fichier
file = fopen('Data/data_pretraitement.txt','r');

line = fscanf(file,'%d %d',[1 2]); % dimension de ma matrice

A = zeros(line(1),line(2)); % matrice contraintes
b = zeros(line(1),1); % vecteur condition


for i=1:1:size(A,1)
    line = fscanf(file,'%d %d',[1 2]);
    A(i,1) = line(1);
    A(i,2) = line(2);
end

for i=1:1:size(A,1)
    line = fscanf(file,'%d',[1 1]);
    b(i) = line(1);
end

nbProd = linprog(f,A,b,[],[],[0,0],[inf,inf]);
nbPanneaux = ceil(nbProd(1));
nbEolienne = ceil(nbProd(2));

