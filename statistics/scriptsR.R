library(readxl)

#Specifying the excel file location
path <- "C:/Users/hp/Documents/X3/U.E_5_Traitement_de_données/Projet_DATA/projet-data/data/sample.xlsx"

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
#Puis on boucle sur chaque élément de la liste afin d'afficher le Mode
lst <- list(Covered_dist, Convergence_Time)
for (i in 1:length(lst)) {
  elmt <- table(lst[[i]])
  mode_function <- rownames(elmt)[which.max(elmt)]
  
  print(paste("Mode for element", i, ":", mode_function))
}

#Draws a histogram of the convergence time then delays for 2 seconds
hist(Convergence_Time, main = "Histogram of Convergence Time", xlab = "Values")
Sys.sleep(2)

#Draws a histogram of the covered distance then delays for 2 seconds
hist(Covered_dist, main = "Histogram of Covered Distance", xlab = "Values")
Sys.sleep(2)

#Draws a mustache box of the Convergence Time features then delays for 2 seconds
boxplot(Convergence_Time, main = "Boxplot Convergence Time", col = c("skyblue"), ylab = "Values", xlab = "Data")
Sys.sleep(2)

#Draws a mustache box of the Covered distance features
boxplot(Covered_dist, main = "Boxplot Covered Distances", col = c("red"), ylab = "Values", xlab = "Data")










