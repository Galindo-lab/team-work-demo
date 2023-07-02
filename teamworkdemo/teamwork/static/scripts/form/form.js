
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

            {
                title: "¿Qué es lo que yo creo que puedo aportar a un equipo?",
                availablePoints: 10,
                points: 0,
                questions: [
                    {
                        label: "Creo que sé ver rápidamente nuevas oportunidades y sacar partido de ellas.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Sé trabajar bien con una amplia variedad de gente.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Producir ideas es una de mis aptitudes personales.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Mi habilidad reside en ser capaz de hacer que las personas hablen cuando detecto que tienen algo de valor con lo que contribuir a los objetivos del grupo.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Mi efectividad personal tiene mucho que ver con mi capacidad para 'seguir hacia delante'.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "No me importa afrontar una impopularidad temporal si esta lleva a resultados que al final merezcan la pena.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Normalmente soy capaz de saber qué es realista y qué tiene posibilidades de funcionar.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Puedo argumentar razonadamente a favor de distintas alternativas de acción excluyentes sin que estén presentes los prejuicios.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Mis comentarios tanto sobre los puntos generales como específicos son siempre bien recibidos.",
                        profile: "tonto",
                        points: 0,
                    },
                ]
            },



            {
                title: "Si tuviera algún problemilla trabajando en equipo, podría ser debido a:",
                availablePoints: 10,
                points: 0,
                questions: [
                    {
                        label: "No estoy a gusto a menos que las reuniones estén bien estructuradas, controladas y generalmente bien conducidas.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Tengo inclinación a ser demasiado generoso hacia otros que tienen un punto de vista válido al que no se le ha prestado suficiente atención.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Cuando en el equipo nos ponemos a buscar nuevas ideas, yo tiendo a hablar demasiado.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Mi punto de vista, más objetivo, hace que me resulte difícil reunirme cómodamente con colegas.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Algunas veces soy visto como enérgico y dominante si se tiene que hacer una cosa.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Encuentro difícil dirigir estando al frente, quizá porque me puedo dejar llevar demasiado por el ambiente del grupo.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Tengo tendencia a ensimismarme en ideas que se me ocurren a mí; y por ello perder el contacto con lo que estamos haciendo.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Mis colegas ven que suelo estar preocupado innecesariamente por los detalles y por la posibilidad de que las cosas vayan mal.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Me cuesta contribuir a menos que el tema tenga algo que ver con algo que conozca bien.",
                        profile: "",
                        points: 0,
                    }
                ]
            },



            {
                title: "Cuando estoy metido en un proyecto con otras personas:",
                availablePoints: 10,
                points: 0,
                questions: [
                    {
                        label: "Tengo capacidad para influir sobre las personas sin presionarlas.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Mi nivel de atención continua me evita cometer tanto omisiones como errores por descuido.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "No dudo en tomar medidas para asegurar que en la reunión no se pierde el tiempo ni se pierden de vista los objetivos.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Se puede contar conmigo para contribuir con algo original.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Estoy siempre dispuesto a respaldar una buena sugerencia de interés para todos.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Me gusta buscar lo último en ideas y desarrollos.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Creo que mi capacidad de juicio puede ayudar a tomar la decisión adecuada.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Se puede confiar en mí para contar con que todo el trato esencial esté organizado.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Se pede tener la seguridad de que seré yo mismo.",
                        profile: "",
                        points: 0,
                    },
                ]
            },

            {
                title: "Obtengo satisfacción de un trabajo porque...",
                availablePoints: 10,
                points: 0,
                questions: [
                    {
                        label: "Disfruto analizando situaciones y sopesando las posibles alternativas.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Me intereso por encontrar soluciones prácticas a los problemas.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Me gusta ver que estoy fomentando buenas relaciones de trabajo.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Sé influir fuertemente en la toma de decisiones.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Sé contactar con gente que podría tener algo nuevo que ofrecer.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Sé poner a la gente de acuerdo en un camino a seguir, si es necesario.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Me siento en mi elemento cuando puedo dedicar toda mi atención a una tarea.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Me gusta encontrar un área que ensanche mi imaginación.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Siento que estoy utilizando mi formación y mis especiales aptitudes para sacar partido de las situaciones.",
                        profile: "",
                        points: 0,
                    },
                ]
            },

            {
                title: "Si de repente me dan la responsabilidad de una tarea difícil, con un tiempo limitado y gente desconocida:",
                availablePoints: 10,
                points: 0,
                questions: [
                    {
                        label: "Me apetecería retirarme a un rincón para idear una salida al problema antes que aplicar una línea de acciones.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Estaría dispuesto a trabajar con la persona que me mostrara la propuesta más positiva.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Encontraría la manera de reducir el tamaño de la tarea discerniendo a qué aspecto contribuirán mejor los diferentes individuos.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Mi sentido natural de la urgencia ayudaría a asegurar que no sobrepasáramos el plazo previsto.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Creo que no me alteraría y mantendría mi capacidad de pensar intacta.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Mantendría invariables los objetivos a pesar de las presiones.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Llevaría de la mano al grupo si viera que no está haciendo ningún progreso.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Fomentaría discusiones de cara a estimular nuevas ideas y hacer que algo empezara a moverse.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Enfocaría todo el problema desde el punto de vista del conocimiento que tuviera sobre el tema.",
                        profile: "",
                        points: 0,
                    },
                ]
            },

            {
                title: "Haciendo referencia a los problemas que tengo trabajando en equipo:",
                availablePoints: 10,
                points: 0,
                questions: [
                    {
                        label: "Suelo mostrar mi impaciencia con aquellos que están impidiendo el progreso.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Los demás podrían criticarme por ser demasiado analítico e insuficientemente intuitivo.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Mi deseo de asegurar que el trabajo se hace de manera adecuada puede suponer un freno.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Tiendo a aburrirme bastante fácilmente y a confiar en uno o dos miembros del grupo interesantes para sacarme del aburrimiento.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Encuentro difícil empezar algo a menos que las metas estén claras.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "A veces soy pobre en la explicación y clarificación de ideas complejas que se me ocurren a mí.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Soy consciente de que pido a los otros las cosas que no puedo hacer por mí mismo.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Dudo en exponer mis puntos de vista cuando me encuentro con una buena oposición.",
                        profile: "",
                        points: 0,
                    },
                    {
                        label: "Me inclino a pensar que estoy perdiendo el tiempo y que lo haría mejor yo solo.",
                        profile: "",
                        points: 0,
                    },
                ]
            },

            // agregar las secciones faltantes...
        ]
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

                    // TODO: Hacer algo más elegante
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
                    points = formData.get(question.profile) + question.points
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
                for (const section of form) {
                    section.points = section.questions.reduce((sum, question) => {
                        return sum + parseInt(question.points);
                    }, 0);
                }

            },
            deep: true
        }
    }
})