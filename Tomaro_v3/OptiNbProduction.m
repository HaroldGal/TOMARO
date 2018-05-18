%% Lecture du fichier

f = [1 10]; %nbPanneaux + nb Eolienne

%Ouverture du fichier
file = fopen('Data/data_pretraitement.txt','r');

line = fscanf(file,'%d %d',[1 2]); % dimension de ma matrice

A = zeros(line(1),line(2)); % matrice contraintes
b = zeros(line(1),1); % vecteur condition


for i=1:1:size(A,1)
    line = fscanf(file,'%d %d',[1 2]);
    A(i,1) = -line(1);
    A(i,2) = -line(2);
end

for i=1:1:size(A,1)
    line = fscanf(file,'%d',[1 1]);
    b(i) = -line(1);
end

%% On enlève 5% des consommations max et 5% des productions min
nb_point = ceil(0.05*length(A));

% On enlève les consommations max
for i=1:nb_point
    [~,index] = max(abs(b));
    b(index) = [];
    A(index,:)=[];
end

A_prod = abs(sum(A,2));

for i=1:nb_point
   [~,index] = max(A_prod);
   b(index) = [];
   A(index,:)=[];
end


%% Optimisation 
nbProd = intlinprog(f,[1 2],A,b,[],[],[0,0],[]);
nbPanneaux = ceil(nbProd(1));
nbEolienne = ceil(nbProd(2));
fclose(file);

file = fopen('nb_devices.txt','w');
fprintf(file,'%d \n%d',nbPanneaux,nbEolienne);
fclose(file);

quit



