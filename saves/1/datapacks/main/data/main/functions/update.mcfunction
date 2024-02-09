datapack disable "file/loader"
datapack enable "file/loader"
# execute store result storage minecraft:main result int 1 run function loader:load
# execute if data storage minecraft:main {result:0} run say Error oh no :(
function main:load
