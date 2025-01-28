const services = document.getElementById("services");
const decrementButtons = services.querySelectorAll(".decrement");
const incrementButtons = services.querySelectorAll(".increment");
const totalElement = document.getElementById("total");
const averageElement = document.getElementById("average");
const countElement = document.getElementById("count");

let total = 0;
let count = 0;
let mainServiceValue = 0;

function updateTotals() {
  totalElement.textContent = `Общая стоимость: ${total}р`;
  const pricePerUnit = mainServiceValue > 0 ? total / mainServiceValue : 0;
  averageElement.textContent = `Цена за единицу: ${pricePerUnit.toFixed(2)}р`;
  // countElement.textContent = `Общее количество услуг: ${count}`;
}

services.addEventListener("click", event => {
  const { target } = event;
  const input = target.parentNode.querySelector("input");
  const value = parseInt(input.value);

  if (target.classList.contains("decrement") && value > 0) {
    input.value = value - 1;
  } else if (target.classList.contains("increment")) {
    input.value = value + 1;
  }

  updateValues();
});

services.addEventListener("input", updateValues);

function updateValues() {
  total = 0;
  count = 0;
  mainServiceValue = 0;

  const serviceElements = services.querySelectorAll(".service");

  serviceElements.forEach(serviceElem => {
    const input = serviceElem.querySelector("input");
    const { textContent: price } = serviceElem.querySelector(".service-price");
    let value = parseInt(input.value);

    if (isNaN(value) || value < 0) {
      value = 0;
      input.value = "0";
    }

    total += parseInt(price) * value;
    count += value;

    if (serviceElem.id === "main") {
      mainServiceValue = value; // Store the value from the input field with id "main"
    }
  });

  const pricePerUnit = (mainServiceValue > 0 ? total / mainServiceValue : 0).toFixed(2);
  averageElement.textContent = `Цена за единицу товара: ${pricePerUnit}р`;

  updateTotals();
}
