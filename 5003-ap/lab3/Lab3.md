**Lab 3  CCGC5003 – Application Programming  Winter 2023** 

**Objective:** 

- Use of functions 
- Use of Dictionary 
- Conditional and Control Statements 
- Passing values in functions and functions returning values 
- Search data 
- Displays formatted information in the form of report display 

**Introduction:** 

This application is implemented to check items in the inventory, add items, display all items, search specific items and it requires item’s serial number to search an item. Information about the item that is stored in the inventory includes item name, item serial number/code, number of items in the inventory and the price per item in the inventory. 

This application uses dictionary to store inventory application.  **Application execution:** 

Menu options are displayed until user chooses to end the application. Following shows the menu options: 

![](Aspose.Words.1abcceb4-df84-402c-b08b-75d8228e7dce.001.jpeg)

Top right hand corner shows your name and student ID. 

If user chooses option 2 to display the inventory items (note, so far no item is added in the inventory), following is displayed: 

“There are no inventory items to display ………“ 

![](Aspose.Words.1abcceb4-df84-402c-b08b-75d8228e7dce.002.jpeg)

The message displayed is “There are no items in inventory to display…….” 

Without adding any item in the inventory, if user chooses option 3 to search an item by its serial code. The message displayed is: 

![](Aspose.Words.1abcceb4-df84-402c-b08b-75d8228e7dce.003.png)

The message displayed is: “There are no items in inventory…..” Application goes back to display the menu options. 

If user chooses an option that is NOT valid option, any numeric or non-numeric value that is not in the list of 1, 2, 3 and 4, following message is displayed: 

“Enter a valid choice…..” 

![](Aspose.Words.1abcceb4-df84-402c-b08b-75d8228e7dce.004.png)

Now user chooses – option 1 to add any item in the inventory. Inventory item consists of following members of the dictionary: 

Item Serial Code is the unique identifier of the item and it cannot be duplicated. Item name, item quantity in stock and item price per unit. 

This information for each item will be saved in a dictionary for each item. 

If user chooses option 1, to add an item, following is displayed: 

![](Aspose.Words.1abcceb4-df84-402c-b08b-75d8228e7dce.005.jpeg)When first item is added to the inventory, then the message displayed is: “Items Inventory does not have any items …. Adding new items” 

A new item is added to the inventory of items. 

Next two diagrams show that two new items are saved in the inventory: 

![](Aspose.Words.1abcceb4-df84-402c-b08b-75d8228e7dce.006.jpeg)

Message displayed is: 

“Searching if item already exists in the items inventory … Item is not in inventory …. Adding new item to inventory ….” 

So before new item is added, system searches for item Serial code if it exists. If item serial code does not exist, then the item is added to the inventory dictionary, as shown in the example above. 

Another item is added to the inventory of items: 

![](Aspose.Words.1abcceb4-df84-402c-b08b-75d8228e7dce.006.jpeg)

Displaying the report of inventory items is option 2 and it displays as follows: 

![](Aspose.Words.1abcceb4-df84-402c-b08b-75d8228e7dce.007.jpeg)If user chooses option 3 to search an item from the inventory based on the serial code, then following is displayed: 

When user enters option 3 to search an item, application asks user to enter the Serial Code for the item to search, user enters the item Serial Code. If the Serial Code, that is the unique identifier, exists, then following is displayed: 

![](Aspose.Words.1abcceb4-df84-402c-b08b-75d8228e7dce.008.jpeg)

Note that there is only one item displayed, as item in the inventory is unique based on item Serial Code. 

If user chooses to search an item based on the Serial Code and Serial code does not exist in the item inventory records, then following message is displayed: 

![](Aspose.Words.1abcceb4-df84-402c-b08b-75d8228e7dce.009.jpeg)Note that item Serial Code “DC246” is not listed in the inventory items so it displays the message:   “Item with Serial Code DC246 is not in inventory ….” 

Option 2 displays the inventory items (saved in the dictionary). 

![](Aspose.Words.1abcceb4-df84-402c-b08b-75d8228e7dce.010.jpeg)

When adding an item in the inventory, if user enters an identical item Serial Code, that is already part of the items inventory (name may or may not be the same), system updates the quantity by taking previous saved quantity in the dictionary and adding a new quantity to the previous value – thus updating the quantity to new value. This is shown below. Note, if the new price entered is less than the previously saved item price per unit, then the lower price is not updated in the inventory records. This is shown below: 

![](Aspose.Words.1abcceb4-df84-402c-b08b-75d8228e7dce.011.png)

Note: Here GC123 (item that is already in the inventory has already saved price of $257.27, which is higher than the new price of $198.7632. Previously saved item values was 12 and new quantity that will be updated is 7, so the new quantity will be (12+7 = 19) 19. 

Price that was already $257.27 will remain as it is. This is shown below: 

![](Aspose.Words.1abcceb4-df84-402c-b08b-75d8228e7dce.011.png)

Displaying the updated Quantity (price does not change): 

![](Aspose.Words.1abcceb4-df84-402c-b08b-75d8228e7dce.012.jpeg)

Say the new inventory items list is displayed as follows: 

![](Aspose.Words.1abcceb4-df84-402c-b08b-75d8228e7dce.013.jpeg)

New item having Serial Code GC123 is added having price of $189.3878 (7 new items). In this case only item in stock quantity is updated, as previously price per item is $258.87. 

![](Aspose.Words.1abcceb4-df84-402c-b08b-75d8228e7dce.014.jpeg)

New quantity is now 31 (old quantity) + 7 (new item quantity) = 38. This is shown below: 

![](Aspose.Words.1abcceb4-df84-402c-b08b-75d8228e7dce.015.jpeg)

Note: In this case the price for the item with Serial Code GC123 did not change and remains $258.87. The Items Quantity changed to 38. 

Now if an item having same Serial Code added with higher item price than that is stored in the inventory, then new higher price is updated in the inventory, along with the new updated total items quantity in stock. This is shown below: 

![](Aspose.Words.1abcceb4-df84-402c-b08b-75d8228e7dce.016.jpeg)

Five new items with Serial Code GC123 are added (making a total of 38+5=43) and therefore total items with Serial Code GC123 becomes 43 and the price per item is also updated to $276.39.  

This is shown below: 

![](Aspose.Words.1abcceb4-df84-402c-b08b-75d8228e7dce.017.jpeg)

If user chooses option 3 to search an item in the inventory, and the item Serial Code does not exist, then following message is displayed: 

![](Aspose.Words.1abcceb4-df84-402c-b08b-75d8228e7dce.018.jpeg)

Message printed is: “Item with Serial Code DC246 is not in inventory …” 

When user chooses option 4, application ends (as shown above), after stating the fact that “Ending application …..” 

**Reports submission:** Lab report to be submitted: 

1) Complete source code (filename) having filename extension “.py” 
1) Execute application and take screenshots of all valid and invalid test cases to test the boundary conditions (as shown in the problem definition above). Crop the screenshots and paste them in a document. Upload PDF format of the document. 

The conditions to be tested: 

1) Enter choice 2 to display inventory, without adding items in the inventory 
1) Enter choice 3 to search and display inventory items, without adding any item in the inventory 
1) Choose option other than the valid choices (1, 2, 3, or 4). It could be alphabet or numeric value 
1) Add two to three items in inventory and display using option 2. 
1) Add an item having identical Serial Code to an existing item in the inventory to show that quantity is updated without updating the item price 
1) Add an item having identical Serial Code to existing item in inventory, but having higher item unit price to show the update in inventory quantity as well as inventory price (unit price) 
1) Search inventory when Item is in the inventory 
1) Search inventory when Item is NOT in the inventory. 
1) Enter valid choice as option as well as invalid choice as an option (to show the messages displayed 
1) Demonstrate how application ends. 

These screenshots (with various options shown above) are pasted and cropped in the document and PDF is uploaded. 

**Rubric for Lab 3:** 

Menu options (with proper conditions and loops – executed in main)   **2 Marks** Different test conditions to add an item in the inventory  **4 Marks** Different test conditions to search an item from inventory  **3 Marks** Application end and other invalid conditions  **1 Mark** Total:   **10 Marks** 
