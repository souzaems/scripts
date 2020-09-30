#First you need to pick the specific shapefile that you want and put in your workdirectory, and work on it
#Use these libraries
library(ggplot2)
library(sf)
library(rnaturalearth)
library(rnaturalearthdata)
library(ggspatial)
library(rgeos)

#You will create a data frame 
world <- ne_countries(scale = "large", returnclass = "sf")

# In my case, I downloaded the shapefiles from IUCN database(shx, dbf, etc.)
# Give a name to my shapefile
shp <- read_sf('MARINE_MAMMALS.shp')
#Select the group that I want to plot
ggplot(shp[which(shp$genus=="Trichechus"),]) + 
  geom_sf(data = world, fill= "antiquewhite") +
  geom_sf(aes(colour = binomial)) +
  coord_sf(xlim = c(-100, 20), ylim = c(-15, 40)) +
  annotation_scale(location = "bl", width_hint = 0.4) +
  annotation_north_arrow(location = "bl", which_north = "true", 
                         pad_x = unit(0.75, "cm"), pad_y = unit(0.5, "cm"),
                         style = north_arrow_fancy_orienteering) +
  theme(panel.grid.major = element_line(linetype = 0), 
        panel.background = element_rect(fill = "aliceblue"),
        legend.title = element_blank(),
        legend.position = c(0.9, 0.9))

#save the figure
ggsave("map_mammal.png", width = 12, height = 6, dpi = 300)
