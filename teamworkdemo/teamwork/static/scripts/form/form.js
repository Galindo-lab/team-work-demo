
new Vue({
    delimiters: ['[[', ']]'],
    el: '#Belbin',
    data: {
        sections: [
            // title: "sección de ejemplo",   Titulo de la sección 
            // availablePoints: 10,           Maximo numero de puntos para repartir
            // points: 0,                     Numero de puntos repartidos
            // questions:
            //   label: "pregunta 1",         Texto de la pregunta 
            //   points: 0,                   Numero de puntos asignados
            //   profile: "plant"             Perfil al que aportan los puntos:
            //                                 - resource_investigator
            //                                 - team_worker
            //                                 - coordinator
            //                                 - plant
            //                                 - monitor_evaluator
            //                                 - specialist
            //                                 - shaper
            //                                 - implementer
            //                                 - completer_finisher

            // 1
            {
                title: "¿Qué es lo que yo creo que puedo aportar a un equipo?",
                availablePoints: 10,
                points: 0,
                questions: [
                    {
                        // 3
                        label: "Creo que sé ver rápidamente nuevas oportunidades y sacar partido de ellas.",
                        profile: "completer_finisher",
                        points: 0,
                    },
                    {
                        // 4
                        label: "Sé trabajar bien con una amplia variedad de gente.",
                        profile: "team_worker",
                        points: 0,
                    },
                    {
                        // 5
                        label: "Producir ideas es una de mis aptitudes personales.",
                        profile: "plant",
                        points: 0,
                    },
                    {
                        // 6
                        label: "Mi habilidad reside en ser capaz de hacer que las personas hablen cuando detecto que tienen algo de valor con lo que contribuir a los objetivos del grupo.",
                        profile: "coordinator",
                        points: 0,
                    },
                    {
                        // 7
                        label: "Mi efectividad personal tiene mucho que ver con mi capacidad para 'seguir hacia delante'.",
                        profile: "resource_investigator",
                        points: 0,
                    },
                    {
                        // 8
                        label: "No me importa afrontar una impopularidad temporal si esta lleva a resultados que al final merezcan la pena.",
                        profile: "shaper",
                        points: 0,
                    },
                    {
                        // 9
                        label: "Normalmente soy capaz de saber qué es realista y qué tiene posibilidades de funcionar.",
                        profile: "implementer",
                        points: 0,
                    },
                    {
                        // 10
                        label: "Puedo argumentar razonadamente a favor de distintas alternativas de acción excluyentes sin que estén presentes los prejuicios.",
                        profile: "monitor_evaluator",
                        points: 0,
                    },
                    {
                        // 11
                        label: "Mis comentarios tanto sobre los puntos generales como específicos son siempre bien recibidos.",
                        profile: "specialist",
                        points: 0,
                    },
                ]
            },

            // 2
            {
                title: "Si tuviera algún problemilla trabajando en equipo, podría ser debido a:",
                availablePoints: 10,
                points: 0,
                questions: [
                    {
                        // 3
                        label: "No estoy a gusto a menos que las reuniones estén bien estructuradas, controladas y generalmente bien conducidas.",
                        profile: "implementer",
                        points: 0,
                    },
                    {
                        // 4
                        label: "Tengo inclinación a ser demasiado generoso hacia otros que tienen un punto de vista válido al que no se le ha prestado suficiente atención.",
                        profile: "coordinator",
                        points: 0,
                    },
                    {
                        // 5
                        label: "Cuando en el equipo nos ponemos a buscar nuevas ideas, yo tiendo a hablar demasiado.",
                        profile: "completer_finisher",
                        points: 0,
                    },
                    {
                        // 6
                        label: "Mi punto de vista, más objetivo, hace que me resulte difícil reunirme cómodamente con colegas.",
                        profile: "monitor_evaluator",
                        points: 0,
                    },
                    {
                        // 7
                        label: "Algunas veces soy visto como enérgico y dominante si se tiene que hacer una cosa.",
                        profile: "shaper",
                        points: 0,
                    },
                    {
                        // 8
                        label: "Encuentro difícil dirigir estando al frente, quizá porque me puedo dejar llevar demasiado por el ambiente del grupo.",
                        profile: "team_worker",
                        points: 0,
                    },
                    {
                        // 9
                        label: "Tengo tendencia a ensimismarme en ideas que se me ocurren a mí; y por ello perder el contacto con lo que estamos haciendo.",
                        profile: "plant",
                        points: 0,
                    },
                    {
                        // 10
                        label: "Mis colegas ven que suelo estar preocupado innecesariamente por los detalles y por la posibilidad de que las cosas vayan mal.",
                        profile: "resource_investigator",
                        points: 0,
                    },
                    {
                        // 11
                        label: "Me cuesta contribuir a menos que el tema tenga algo que ver con algo que conozca bien.",
                        profile: "specialist",
                        points: 0,
                    }
                ]
            },

            // 3
            {
                title: "Cuando estoy metido en un proyecto con otras personas:",
                availablePoints: 10,
                points: 0,
                questions: [
                    {
                        // 3
                        label: "Tengo capacidad para influir sobre las personas sin presionarlas.",
                        profile: "coordinator",
                        points: 0,
                    },
                    {
                        // 4
                        label: "Mi nivel de atención continua me evita cometer tanto omisiones como errores por descuido.",
                        profile: "resource_investigator",
                        points: 0,
                    },
                    {
                        // 5
                        label: "No dudo en tomar medidas para asegurar que en la reunión no se pierde el tiempo ni se pierden de vista los objetivos.",
                        profile: "shaper",
                        points: 0,
                    },
                    {
                        // 6
                        label: "Se puede contar conmigo para contribuir con algo original.",
                        profile: "plant",
                        points: 0,
                    },
                    {
                        // 7
                        label: "Estoy siempre dispuesto a respaldar una buena sugerencia de interés para todos.",
                        profile: "team_worker",
                        points: 0,
                    },
                    {
                        // 8
                        label: "Me gusta buscar lo último en ideas y desarrollos.",
                        profile: "completer_finisher",
                        points: 0,
                    },
                    {
                        // 9
                        label: "Creo que mi capacidad de juicio puede ayudar a tomar la decisión adecuada.",
                        profile: "monitor_evaluator",
                        points: 0,
                    },
                    {
                        // 10
                        label: "Se puede confiar en mí para contar con que todo el trato esencial esté organizado.",
                        profile: "implementer",
                        points: 0,
                    },
                    {
                        // 11
                        label: "Se pede tener la seguridad de que seré yo mismo.",
                        profile: "specialist",
                        points: 0,
                    },
                ]
            },

            // 4
            {
                title: "Mi forma de abordar el trabajo en equipo es: ",
                availablePoints: 10,
                points: 0,
                questions: [
                    {
                        // 3
                        label: "Tengo bastante interés en conocer mejor a los colegas.",
                        profile: "team_worker",
                        points: 0,
                    },
                    {
                        // 4
                        label: "Soy reacio a dar una oportunidad a los puntos de vista de otros o a apoyar el punto de vista de una minoría.",
                        profile: "shaper",
                        points: 0,
                    },
                    {
                        // 5
                        label: "Generalmente encuentro un argumento con el que refutar proposiciones poco firmes.",
                        profile: "monitor_evaluator",
                        points: 0,
                    },
                    {
                        // 6
                        label: "Creo que tengo talento para hacer que funcionen las cosas una vez tiene que ponerse en práctica un plan.",
                        profile: "implementer",
                        points: 0,
                    },
                    {
                        // 7
                        label: "Tengo tendencia a evitar lo obvio y salir con lo inesperado.",
                        profile: "plant",
                        points: 0,
                    },
                    {
                        // 8
                        label: "Aporto un toque de perfección a todo el trabajo que dirijo.",
                        profile: "resource_investigator",
                        points: 0,
                    },
                    {
                        // 9
                        label: "Hago uso de contactos ajenos al grupo en sí mismo.",
                        profile: "completer_finisher",
                        points: 0,
                    },
                    {
                        // 10
                        label: "Al mismo tiempo que estoy interesado en todos los puntos de vista, no tengo ningún problema cuando la decisión ha de ser tomada. ",
                        profile: "coordinator",
                        points: 0,
                    },
                    {
                        // 11
                        label: "Contribuyo cuando realmente sé del tema.",
                        profile: "specialist",
                        points: 0,
                    },
                ]
            },

            // 5
            {
                title: "Obtengo satisfacción de un trabajo porque...",
                availablePoints: 10,
                points: 0,
                questions: [
                    {
                        // 3
                        label: "Disfruto analizando situaciones y sopesando las posibles alternativas.",
                        profile: "monitor_evaluator",
                        points: 0,
                    },
                    {
                        // 4
                        label: "Me intereso por encontrar soluciones prácticas a los problemas.",
                        profile: "implementer",
                        points: 0,
                    },
                    {
                        // 5
                        label: "Me gusta ver que estoy fomentando buenas relaciones de trabajo.",
                        profile: "team_worker",
                        points: 0,
                    },
                    {
                        // 6
                        label: "Sé influir fuertemente en la toma de decisiones.",
                        profile: "shaper",
                        points: 0,
                    },
                    {
                        // 7
                        label: "Sé contactar con gente que podría tener algo nuevo que ofrecer.",
                        profile: "completer_finisher",
                        points: 0,
                    },
                    {
                        // 8
                        label: "Sé poner a la gente de acuerdo en un camino a seguir, si es necesario.",
                        profile: "coordinator",
                        points: 0,
                    },
                    {
                        // 9
                        label: "Me siento en mi elemento cuando puedo dedicar toda mi atención a una tarea.",
                        profile: "resource_investigator",
                        points: 0,
                    },
                    {
                        // 10
                        label: "Me gusta encontrar un área que ensanche mi imaginación.",
                        profile: "plant",
                        points: 0,
                    },
                    {
                        // 11
                        label: "Siento que estoy utilizando mi formación y mis especiales aptitudes para sacar partido de las situaciones.",
                        profile: "specialist",
                        points: 0,
                    },
                ]
            },

            // 6
            {
                title: "Si de repente me dan la responsabilidad de una tarea difícil, con un tiempo limitado y gente desconocida:",
                availablePoints: 10,
                points: 0,
                questions: [
                    {
                        // 3
                        label: "Me apetecería retirarme a un rincón para idear una salida al problema antes que aplicar una línea de acciones.",
                        profile: "plant",
                        points: 0,
                    },
                    {
                        // 4
                        label: "Estaría dispuesto a trabajar con la persona que me mostrara la propuesta más positiva.",
                        profile: "team_worker",
                        points: 0,
                    },
                    {
                        // 5
                        label: "Encontraría la manera de reducir el tamaño de la tarea discerniendo a qué aspecto contribuirán mejor los diferentes individuos.",
                        profile: "coordinator",
                        points: 0,
                    },
                    {
                        // 6
                        label: "Mi sentido natural de la urgencia ayudaría a asegurar que no sobrepasáramos el plazo previsto.",
                        profile: "resource_investigator",
                        points: 0,
                    },
                    {
                        // 7
                        label: "Creo que no me alteraría y mantendría mi capacidad de pensar intacta.",
                        profile: "monitor_evaluator",
                        points: 0,
                    },
                    {
                        // 8
                        label: "Mantendría invariables los objetivos a pesar de las presiones.",
                        profile: "implementer",
                        points: 0,
                    },
                    {
                        // 9
                        label: "Llevaría de la mano al grupo si viera que no está haciendo ningún progreso.",
                        profile: "shaper",
                        points: 0,
                    },
                    {
                        // 10
                        label: "Fomentaría discusiones de cara a estimular nuevas ideas y hacer que algo empezara a moverse.",
                        profile: "completer_finisher",
                        points: 0,
                    },
                    {
                        // 11
                        label: "Enfocaría todo el problema desde el punto de vista del conocimiento que tuviera sobre el tema.",
                        profile: "specialist",
                        points: 0,
                    },
                ]
            },

            // 7
            {
                title: "Haciendo referencia a los problemas que tengo trabajando en equipo:",
                availablePoints: 10,
                points: 0,
                questions: [
                    {
                        // 3
                        label: "Suelo mostrar mi impaciencia con aquellos que están impidiendo el progreso.",
                        profile: "shaper",
                        points: 0,
                    },
                    {
                        // 4
                        label: "Los demás podrían criticarme por ser demasiado analítico e insuficientemente intuitivo.",
                        profile: "monitor_evaluator",
                        points: 0,
                    },
                    {
                        // 5
                        label: "Mi deseo de asegurar que el trabajo se hace de manera adecuada puede suponer un freno.",
                        profile: "resource_investigator",
                        points: 0,
                    },
                    {
                        // 6
                        label: "Tiendo a aburrirme bastante fácilmente y a confiar en uno o dos miembros del grupo interesantes para sacarme del aburrimiento.",
                        profile: "completer_finisher",
                        points: 0,
                    },
                    {
                        // 7
                        label: "Encuentro difícil empezar algo a menos que las metas estén claras.",
                        profile: "implementer",
                        points: 0,
                    },
                    {
                        // 8
                        label: "A veces soy pobre en la explicación y clarificación de ideas complejas que se me ocurren a mí.",
                        profile: "plant",
                        points: 0,
                    },
                    {
                        // 9
                        label: "Soy consciente de que pido a los otros las cosas que no puedo hacer por mí mismo.",
                        profile: "coordinator",
                        points: 0,
                    },
                    {
                        // 10
                        label: "Dudo en exponer mis puntos de vista cuando me encuentro con una buena oposición.",
                        profile: "team_worker",
                        points: 0,
                    },
                    {
                        // 11
                        label: "Me inclino a pensar que estoy perdiendo el tiempo y que lo haría mejor yo solo.",
                        profile: "specialist",
                        points: 0,
                    },
                ]
            },

            // agregar las secciones faltantes...
        ]
    },

    mounted() {

        for (const section of this.sections) {
            for (question of section.questions) {
                console.log(question)
                question.points = parseInt(question.points) === 0 ? "" : question.points
            }
        }

    },

    methods: {
        submitForm(event) {
            // acciones cuando se presiona aceptar
            event.preventDefault();

            for (const section of this.sections) {
                if (section.points !== section.availablePoints) {
                    // si la cantidad de puntos distribuidos es diferente
                    // a los puntos disponibles, enviar un error 
                    alert("error en la seccion " + section.title)
                    return
                }
            }

            // obtener el elemento seleccionado
            var form = event.target;

            // extraer el csrf del formulario (para las peticiones a django)
            var csrfToken = form.elements.csrfmiddlewaretoken.value;

            // convertir el formulario al modelo del 'BelbinUserProfile'
            var BelbinForm = this.belbinProfile()


            // Agrega el token CSRF a la cabecera de la solicitud
            var headers = {
                'X-CSRFToken': csrfToken
            };

            fetch(form.action, {
                method: 'POST',
                body: BelbinForm,
                headers: headers
            }).then((response) => {
                // Maneja la respuesta del servidor
                if (response.ok) {
                    console.log("Solicitud POST exitosa");

                    // TODO: Mostrar la pantalla de resultados
                    location.reload()
                } else {
                    console.error("Error en la solicitud POST");
                }
            }).catch((error) => {
                console.error("Error en la solicitud POST:", error);
            });

        },

        belbinProfile() {
            // convierte los resultados a un modelo 'BelbinUserProfile'
            var formData = new FormData();

            // agregar los perfiles al form agrega 
            // redundiancia (la repeticion es aproposito)
            formData.append('resource_investigator', 0);
            formData.append('team_worker', 0);
            formData.append('coordinator', 0);
            formData.append('plant', 0);
            formData.append('monitor_evaluator', 0);
            formData.append('specialist', 0);
            formData.append('shaper', 0);
            formData.append('implementer', 0);
            formData.append('completer_finisher', 0);

            // lista de perfiles
            const profiles = [
                'resource_investigator',
                'team_worker',
                'coordinator',
                'plant',
                'monitor_evaluator',
                'specialist',
                'shaper',
                'implementer',
                'completer_finisher'
            ]

            for (const section of this.sections) {
                for (const question of section.questions) {

                    if (!profiles.includes(question.profile)) {
                        // si el perfil no existe se omite
                        console.log(`El perfil ${question.profile} no existe, se omitira su informacion`)
                        continue
                    }

                    // incrementar los puntos 
                    points = Number(formData.get(question.profile)) + Number(question.points)
                    formData.set(question.profile, points)
                }
            }

            return formData
        }
    },
    watch: {
        sections: {
            handler(form) {

                // actualizar los puntos en cada seccion 
                for (section of form) {

                    section.points = section.questions.reduce((sum, question) => {
                        return sum + Number(question.points);
                    }, 0);

                    for (question of section.questions) {
                        console.log(question)
                        question.points = parseInt(question.points) === 0 ? "" : question.points
                    }
                }

            },
            deep: true
        },

    }
})