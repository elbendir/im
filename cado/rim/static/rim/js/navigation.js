document.addEventListener("DOMContentLoaded", function () {
    // Sélectionner tous les éléments ayant la classe 'pcoded-hasmenu'
    const menuItems = document.querySelectorAll(".pcoded-hasmenu");

    // Ajouter un événement de clic à chaque élément de menu
    menuItems.forEach((menuItem) => {
        const link = menuItem.querySelector(".nav-link");
        if (link) {
            link.addEventListener("click", function (e) {
                e.preventDefault(); // Empêche le comportement par défaut du lien
                menuItem.classList.toggle("active"); // Ajoute ou enlève la classe 'active'
            });
        }
    });
});

document.querySelectorAll(".dropdown-btn").forEach(button => {
    button.addEventListener("click", function () {
        this.classList.toggle("active");
        const dropdownContent = this.nextElementSibling;
        dropdownContent.style.display = dropdownContent.style.display === "block" ? "none" : "block";
    });
});


// Fonction pour gérer l'affichage des sous-listes
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".toggle-list").forEach(toggleLink => {
        toggleLink.addEventListener("click", function (event) {
            event.preventDefault();
            const subMenu = this.nextElementSibling;
            if (subMenu) {
                subMenu.style.display = subMenu.style.display === "block" ? "none" : "block";
            }
        });
    });
});

// #############################################################
//replace le nom des variables
// Fonction pour formater le nom de colonne et mettre la majuscule au premier caractère de chaque mot
function formatColumnName(columnName) {
    return columnName
        .replace(/_/g, ' ')
        .replace(/\b\w/g, char => char.toUpperCase());  // Met en majuscule le premier caractère de chaque mot
}

// Fonction pour mettre à jour l'affichage des colonnes
function updateMenuDisplay() {
    document.querySelectorAll('a[data-column]').forEach(function(link) {
        const columnName = link.getAttribute('data-column');
        link.textContent = formatColumnName(columnName);
    });
}

document.addEventListener("DOMContentLoaded", updateMenuDisplay);



// #####################################################
// Initialisation de la variable de type de graphique
let currentChartType = 'line';

// Fonction pour changer le type de graphique
function changeChartType(newType) {
    if (myChart.config.type !== newType) {
        // Modifier le type de graphique
        myChart.config.type = newType;
        myChart.update();
    }

    // Mettre à jour l'état visuel des boutons
    document.querySelectorAll('.chart-button').forEach(button => button.classList.remove('active'));
    
    // Marquer le bouton actif
    document.getElementById(newType + 'ChartButton').classList.add('active');
}

// Fonction pour mettre à jour le graphique avec des données
function updateChartc(type, column = 'default') {
    const dataToDisplay = type === 'volume' ? volumeData[column] : valeurData[column];

    myChart.data.datasets = [{
        label: `Données de ${type} - ${column}`,
        data: dataToDisplay,
        backgroundColor: 'grey',
        borderColor: 'black',
        borderWidth: 1
    }];

    myChart.update();
}


// Fonction pour mettre à jour le graphique avec des données
function updateChartm(type, column = 'default') {
    const dataToDisplay = type === 'volume' ? volumemData[column] : valeurmData[column];

    myChart.data.datasets = [{
        label: `Données de ${type} - ${column}`,
        data: dataToDisplay,
        backgroundColor: 'grey',
        borderColor: 'black',
        borderWidth: 1
    }];

    myChart.update();
}


// Fonction pour mettre à jour le graphique avec des données
function updateChartl(type, column = 'default') {
    const dataToDisplay = type === 'volume' ? volumelData[column] : valeurlData[column];

    myChart.data.datasets = [{
        label: `Données de ${type} - ${column}`,
        data: dataToDisplay,
        backgroundColor: 'grey',
        borderColor: 'black',
        borderWidth: 1
    }];

    myChart.update();
}

// Initialisation : ajouter la classe active au bouton initial
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById('lineChartButton').classList.add('active');
});



// ###############################################filtrer#############################33
document.addEventListener("DOMContentLoaded", function () {
    const startMonthSelect = document.getElementById("startMonth");
    const endMonthSelect = document.getElementById("endMonth");
    const filterButton = document.querySelector(".filter-button");

    filterButton.addEventListener("click", function (event) {
        event.preventDefault(); // Empêcher le rechargement de la page

        const startMonth = startMonthSelect.value;
        const endMonth = endMonthSelect.value;

        // Vérifier si les valeurs sont valides
        if (!startMonth || !endMonth) {
            alert("Veuillez sélectionner une plage de mois valide.");
            return;
        }

        // Filtrer les données en fonction des mois sélectionnés
        updateChartWithFilter(startMonth, endMonth);
    });
});

function updateChartWithFilter(startMonth, endMonth) {
    // Trouver les indices des mois dans l'ordre défini
    const startIndex = mois.indexOf(startMonth);
    const endIndex = mois.indexOf(endMonth);

    if (startIndex === -1 || endIndex === -1 || startIndex > endIndex) {
        alert("Sélection de mois invalide.");
        return;
    }

    // Extraire les mois filtrés
    const filteredMonths = mois.slice(startIndex, endIndex + 1);

    // Filtrer les datasets en fonction des mois sélectionnés
    const newDatasets = myChart.data.datasets.map(dataset => {
        const newData = dataset.data.slice(startIndex, endIndex + 1);
        return { ...dataset, data: newData };
    });

    // Mettre à jour le graphique
    myChart.data.labels = filteredMonths;
    myChart.data.datasets = newDatasets;
    myChart.update();
}
