# Heap 

A heap is a specialized tree-based data structure in computer science that satisfies the heap property. It is commonly implemented as a binary heap, where each parent node has a value greater than or equal to its children (max heap) or less than or equal to its children (min heap). The heap property allows for efficient extraction of the maximum (or minimum) element and efficient insertion of new elements.

<hr>
<br>

## Max Heap and Min Heap
### Max heap

* The root is having the biggest element, when comparing with the descendents 
* It is a complete binary tree
#### **Insertion**
* The element is inserted as a leaf to the left side of the tree.
* It is inserted into the left side in order to preserve the complete binary tree property
* It is then adjusted by comparing it with the root.
* Adjustment is made from leaf towards root.

> Time complexity : **O(1) to O(log n)** , swapping is based of height of the tree

#### **Deletion**
* Only root element is deleted
* The remaining elements are adjusted in a way to preserve the complete binary tree property
* The last element is swapped with the deleted root element
* Then the remaining elements are adjusted to maintain max heap
* The adjustment is made from root towards leaf
> Time complexity : **O(1) to O(log n)** ,depending on the height of the tree and the need for swapping.


```
When an element is deleted, an empty location is created in the last location. 
It is an empty location. The recently deleted element can be stored in that empty location(last array location).
This last location is outside of heap.
```

### Min Heap
* In a min heap, the root holds the smallest element when comparing it with its descendants.
* Similar to a max heap, it is also a complete binary tree.
#### **Insertion**:
* To maintain the complete binary tree property, the new element is inserted as a leaf on the left side of the tree.
* This left-side insertion ensures that the tree remains complete.
* After insertion, the element is adjusted by comparing it with its parent nodes.
* The adjustment process starts from the leaf and moves towards the root.
* If the new element is smaller than its parent, they are swapped to maintain the min heap property.
> Time complexity: **O(1) to O(log n),** depending on the height of the tree and the need for swapping.

#### **Deletion:**
* In a min heap, only the root element is deleted.
* After deletion, the remaining elements are adjusted to preserve the complete binary tree property.
* The last element in the heap is swapped with the deleted root element.
* Then, the remaining elements are adjusted to maintain the min heap property.
* The adjustment process starts from the root and moves towards the leaf.
* Swapping is performed as necessary to ensure that the smaller elements bubble up towards the top.
> Time complexity: **O(1) to O(log n),** depending on the height of the tree and the requirement for swapping.
```
When an element is deleted, an empty space is created in the last location of the heap.
This empty space is located outside of the actual heap structure.
The recently deleted element can be stored in this last location, allowing for efficient memory management.
```

<hr>
<br>

## Relationship between Array Indexes and Tree Elements
If the index of any element in the array is *i*, the element in the index *2i+1* will become the left child and element in *2i+2* index will become the right child.

* i = index of the element
* 2i+1 = left child
* 2i+2 = right child

![image](images/relationship_bw_array_and_heap.png)

* Root element: 1 is the root element in the 0th index posistion.
* In the first row,  the value of i is 0.
* Left element: (2i+1) ie, (2*0+1) ==> 1st index posistion of the element. ==> 12.
* Right element: (2i+2) ==> (2*0+2) ==>  2nd index posistion. ==> 9.


