// VARIABLES
/// HTML Elements
//// Todo Creator
const todoDescriptorInput = document.getElementsByClassName("todo-descriptor-input")[0];
const todoAddButton = document.getElementsByClassName("todo-add-button")[0];
//// Todo List
const todoList = document.getElementsByClassName("todo-list")[0];


// TODO CREATION
function addTodo(){
    if(todoDescriptorInput.value === ""){
        alert("You Must Write Something!");
        return;
    }

    let newTodo = document.createElement("li");
    newTodo.innerHTML = todoDescriptorInput.value;
    todoList.appendChild(newTodo);
    todoDescriptorInput.value = "";
}