const API_URL = 'https://api.api-ninjas.com/v1/hobbies?category=general'
const API_KEY = '6m5f06+C57VCFOCuTYsI+Q==ltfav1xa4MWifHz9';

// Obtener referencias a los elementos del DOM
const hobbyElement = document.getElementById('hobby');
const linkContainer = document.getElementById('link-container');
const categorySelect = document.getElementById('category-select');

// Función para obtener un hobby de la API
async function getHobby() {
  // Limpiar enlace previo
  linkContainer.innerHTML = '';

  // Obtener la categoría seleccionada
  const selectedCategory = categorySelect.value;
  const API_URL = `https://api.api-ninjas.com/v1/hobbies?category=${selectedCategory}`;

  try {
    const response = await fetch(API_URL, {
      headers: { 'X-Api-Key': API_KEY }
    });

    if (response.ok) {
      const data = await response.json();
      const hobby = data.hobby; // Asumiendo que siempre hay un hobby en el array

      // Mostrar el hobby
      hobbyElement.textContent = hobby;

      // Crear el enlace al artículo de Wikipedia
      const link = document.createElement('a');
      link.href = data.link;
      link.textContent = 'Learn more on Wikipedia';
      link.target = '_blank'; // Abrir en una nueva pestaña
      linkContainer.appendChild(link);
    } else {
      hobbyElement.textContent = 'Failed to load hobby.';
    }
  } catch (error) {
    hobbyElement.textContent = 'Error fetching hobby.';
  }
}