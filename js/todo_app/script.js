// VARIABLES
/// HTML Elements
//// Todo Creator
const todoDescriptorInput = document.querySelector(".todo-descriptor-input");
const todoAddButton = document.querySelector(".todo-add-button");
//// Todo List
const todoList = document.querySelector(".todo-list");


// INITIALISATION
///Clickable Objects
todoList.addEventListener("click", modifyTodoItem, false);

///Populate
loadData()


// LOCAL DATA
function saveData(){
    localStorage.setItem("todo-items", todoList.innerHTML);
}

function loadData(){
    todoList.innerHTML = localStorage.getItem("todo-items");
}


// TODO FUNCTIONS
/// Creation
//// Create new html list todo item
function createTodo() {
    const newTodo = document.createElement("li");
    newTodo.innerHTML = todoDescriptorInput.value;
    const deleteButton = document.createElement("span");
    deleteButton.className = "delete-todo-button"
    deleteButton.innerHTML = "\u00d7"; // \u00d7 is icon code for x
    newTodo.appendChild(deleteButton)
    return newTodo
}
//// Add new todo item to todo list
function addTodo(){
    todoList.appendChild(createTodo());
    /// Clear the input field
    todoDescriptorInput.value = "";
    /// Save
    saveData();
}
//// Check if todo text is valid
function checkAddTodo(){
    // Make sure input isn't empty
    if(todoDescriptorInput.value === ""){
        alert("You Must Write Something!");
        return;
    }

    addTodo();
}

/// Modifying
function modifyTodoItem(event){
    const clickedTarget = event.target;
    switch(clickedTarget.tagName){
        case "LI":
            clickedTarget.classList.toggle("todo-item-checked");
            break;
        case "SPAN":
            clickedTarget.parentElement.remove();
            break; 
    }
    saveData();
}