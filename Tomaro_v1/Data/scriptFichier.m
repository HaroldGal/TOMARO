mamatrice=generateur_conso([1,1,0,0,2,2]);
f= fopen('conso.txt','w');
fprintf(f,'Ordinateur:');
dlmwrite('conso.txt',mamatrice(1,:),'delimiter', '','-append');
fseek(f,0,'eof');
fprintf(f,'Television:');
dlmwrite('conso.txt',mamatrice(2,:),'delimiter', '','-append');
fseek(f,0,'eof');
fprintf(f,'Frigidaire:');
dlmwrite('conso.txt',mamatrice(3,:),'delimiter', '','-append');
fseek(f,0,'eof');
fprintf(f,'Chauffage:');
dlmwrite('conso.txt',mamatrice(4,:),'delimiter', '','-append');
fseek(f,0,'eof');
fprintf(f,'GrillePain:');
dlmwrite('conso.txt',mamatrice(5,:),'delimiter', '','-append');
fseek(f,0,'eof');
fprintf(f,'MicroOndes:');
dlmwrite('conso.txt',mamatrice(6,:),'delimiter', '','-append');
fseek(f,0,'eof');
fclose('all')