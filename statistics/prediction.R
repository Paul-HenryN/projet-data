library(ggplot2)
library(readxl)

# import the sample and set the path
path_file = "C:/Users/hp/Documents/X3/U.E_5_Traitement_de_données/Projet_DATA/projet-data/data/sample.xlsx"

#Accessing the excel file using R 
data_file <- read_excel(path_file)

# set the file name as the current variable
attach(data_file)

# calculate the linear regression between two caracters
fit <- lm(Convergence_Time ~ Clients_no, data = data_file)

# draw the linear regression between two caracters
plot(Clients_no, Convergence_Time)
abline(fit)

ggplot(data_file, aes(x = Clients_no, y = Convergence_Time)) + geom_point() + geom_smooth(method = "lm") 

# predict values for larger instances
new_instance <- data.frame(Clients_no=50)
predict(fit, new_instance)