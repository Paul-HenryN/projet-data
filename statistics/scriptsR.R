library(readxl)


#Specifying the excel file location
path <- "C:/Users/hp/Documents/X3/U.E_5_Traitement_de_données/Projet_DATA/projet-data/excelFile.xlsx"

#Accessing the excel file using R 
dataFile <- read_excel(path)

#Attaching the data base(Excel file) to R's search path
attach(dataFile)

#Renders various model fitting functions according to the data entries
summary(dataFile)

#Shows the standard deviation of a chosen caracter
sd(Covered_dist)
sd(Convergence_Time)


#Création d'une liste avec les caractères à étudier
#Puis on boucle sur chaque élément de la lsite afin d'afficher le :
# Mode , Histogramme , Boîte à moustache
lst <- list(Covered_dist, Convergence_Time)
for (i in 1:length(lst)) {
  elmt <- table(lst[[i]])
  mode_function <- rownames(elmt)[which.max(elmt)]
  
  print(paste("Mode for element", i, ":", mode_function))
  hist(x=i, main = "Histogram of Results", xlab = "Values")
  boxplot(i, main ="Boxplot", ylab = "Valeurs", xlab = "Groupe")
}




