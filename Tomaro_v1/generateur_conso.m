function [mat_finale] = generateur_conso(vec_appareils)
% En entree on va avoir un vecteur correspondant au nombre et leur mode de
% consommation 0 : continu 1 : Appareil de jour long (ordinateur
% television,cuisiniere
%2 : appareil de jour court grille pain, micro-onde ... 
% En sortie on a une matrice avec en colonnes les différentes secondes, en
% ligne les appareils, et les valeurs correspondent à si notre appareil est
% alummé ou non 
nb_appareils=length(vec_appareils);
mat_finale=zeros(nb_appareils,86400);
for i=1:nb_appareils
    if vec_appareils(i)==0
        mat_finale(i,:)=ones(1,86400);
        
    
    elseif vec_appareils(i)==1
          stocksecondeinit=14400;
          stockseconde=14400;
          while stockseconde >0
          debututil=randi([25200,82800]);
          tempsutilisation=randi([1800,stocksecondeinit]);
          for j=debututil:1:tempsutilisation+debututil
              mat_finale(i,j)=1;

          end
          stockseconde=stockseconde-tempsutilisation;
          end
    elseif vec_appareils(i)==2
           stocksecondeinit=3600;
          stockseconde=3600;
          while stockseconde >0
          debututil=randi([25200,82800]);
          tempsutilisation=randi([30,3600]);
          for j=debututil:1:tempsutilisation+debututil
              mat_finale(i,j)=1;

          end
          stockseconde=stockseconde-tempsutilisation;
          end
        
        
        
    end
    
    
end



end

