/* =========================================
   VIDEOGAMES NEWS - JAVASCRIPT
   ========================================= */


/* =========================================
   NAVBAR
   ========================================= */

window.addEventListener("DOMContentLoaded", () => {

    const mainNav = document.getElementById("mainNav");

    if (mainNav) {

        const navbarShrink = () => {

            if (window.scrollY === 0) {
                mainNav.classList.remove("navbar-shrink");
            } else {
                mainNav.classList.add("navbar-shrink");
            }

        };

        navbarShrink();

        document.addEventListener("scroll", navbarShrink);

    }


    /* =========================================
       FILTRO DE NOTICIAS
       ========================================= */

    const filterButtons = document.querySelectorAll(".news-filter");
    const newsItems = document.querySelectorAll(".news-item");

    if (filterButtons.length > 0 && newsItems.length > 0) {

        filterButtons.forEach(button => {

            button.addEventListener("click", () => {

                const category = button.dataset.category;


                /* Cambiar botón activo */

                filterButtons.forEach(btn => {
                    btn.classList.remove("active");
                });

                button.classList.add("active");


                /* Filtrar noticias */

                newsItems.forEach(item => {

                    const itemCategory = item.dataset.category;

                    if (
                        category === "todas" ||
                        itemCategory === category
                    ) {

                        item.style.display = "";

                    } else {

                        item.style.display = "none";

                    }

                });

            });

        });

    }


    /* =========================================
       MODAL DE NOTICIAS
       ========================================= */

    const newsButtons = document.querySelectorAll(".news-button");

    const newsModalElement = document.getElementById("newsModal");

    if (newsButtons.length > 0 && newsModalElement) {

        const newsModal = new bootstrap.Modal(newsModalElement);


        /* Información de cada noticia */

        const newsData = {

            noticia1: {
                title: "Nuevos lanzamientos que llegan al mundo gamer",
                category: "LANZAMIENTOS",
                date: "22 de septiembre de 2026",
                text: "El mundo de los videojuegos continúa recibiendo nuevos títulos y experiencias para los jugadores. Durante las próximas semanas se esperan diferentes lanzamientos que buscan destacar por su propuesta, jugabilidad y contenido."
            },

            noticia2: {
                title: "Novedades y movimientos en la industria",
                category: "INDUSTRIA",
                date: "21 de septiembre de 2026",
                text: "La industria de los videojuegos continúa evolucionando con nuevos proyectos, anuncios y movimientos por parte de distintas compañías. Estos cambios forman parte de una industria que constantemente busca nuevas formas de entretener a los jugadores."
            },

            noticia3: {
                title: "Los próximos eventos del mundo de los videojuegos",
                category: "EVENTOS",
                date: "20 de septiembre de 2026",
                text: "Durante el año se realizan diferentes eventos relacionados con los videojuegos. Estas instancias permiten conocer nuevos proyectos, recibir anuncios y descubrir algunas de las novedades que preparan las compañías para los jugadores."
            },

            noticia4: {
                title: "Nuevas actualizaciones llegan a varios videojuegos",
                category: "ACTUALIZACIONES",
                date: "19 de septiembre de 2026",
                text: "Las actualizaciones permiten que los videojuegos continúen evolucionando después de su lanzamiento. Entre las novedades pueden encontrarse nuevos contenidos, mejoras de rendimiento, correcciones y cambios destinados a mejorar la experiencia de los jugadores."
            },

            noticia5: {
                title: "Las compañías continúan preparando nuevos proyectos",
                category: "INDUSTRIA",
                date: "18 de septiembre de 2026",
                text: "Las compañías desarrolladoras y editoras continúan trabajando en nuevos proyectos. Algunos de ellos todavía no han sido presentados completamente al público, mientras que otros comienzan a mostrar sus primeras novedades."
            },

            noticia6: {
                title: "Lo que se viene para los jugadores",
                category: "LANZAMIENTOS",
                date: "17 de septiembre de 2026",
                text: "Los próximos meses traerán diferentes propuestas para los jugadores. Nuevas aventuras, experiencias y géneros estarán disponibles para quienes buscan descubrir nuevos videojuegos."
            }

        };


        /* Abrir modal */

        newsButtons.forEach(button => {

            button.addEventListener("click", () => {

                const newsId = button.dataset.news;

                const news = newsData[newsId];

                if (!news) {
                    return;
                }


                /* Insertar información */

                document.getElementById("newsModalTitle").textContent =
                    news.title;

                document.getElementById("newsModalCategory").textContent =
                    news.category;

                document.getElementById("newsModalDate").textContent =
                    news.date;

                document.getElementById("newsModalText").textContent =
                    news.text;


                /* Mostrar modal */

                newsModal.show();

            });

        });

    }

});