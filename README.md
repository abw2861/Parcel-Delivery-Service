# c950PythonProject
c950 complete project

SCENARIO
A parcel delivery service needs to determine an efficient route and delivery distribution for their Daily Local Deliveries (DLD) 
because packages are not currently being consistently delivered by their promised deadline. 
The route has three trucks, two drivers, and an average of 40 packages to deliver each day. 
Each package has specific criteria and delivery requirements.


For this project, I implemented a greedy algorithm solution, where all 40 packages are delivered on time while also meeting each package's specific requirements. The total combined distance traveled by the trucks is required to stay under 140 miles.


ASSUMPTIONS
 Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.

•   The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.

•   There are no collisions.

•   Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.

•   Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. 

•   The delivery and loading times are instantaneous, i.e., no time passes while at a delivery or when moving packages to a truck at the hub (that time is factored into the calculation of the average speed of the trucks).

•   There is up to one special note associated with a package.

•   The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S State St., Salt Lake City, UT 84111) until 10:20 a.m.

•   The distances provided in the WGUPS Distance Table are equal regardless of the direction traveled.

•   The day ends when all 40 packages have been delivered.
