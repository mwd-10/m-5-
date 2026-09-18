// =========================================================
// DOM ELEMENTS
// =========================================================

const materialA = document.getElementById("materialA");
const materialB = document.getElementById("materialB");

const liquidA = document.getElementById("liquidA");
const liquidB = document.getElementById("liquidB");

const labelA = document.getElementById("labelA");
const labelB = document.getElementById("labelB");

const formulaA = document.getElementById("formulaA");
const formulaB = document.getElementById("formulaB");

const pairNumberA = document.getElementById("pairNumberA");
const pairNumberB = document.getElementById("pairNumberB");

const mixButton = document.getElementById("mixButton");
const newExperiment = document.getElementById("newExperiment");

const resultSection = document.getElementById("resultSection");
const resultTitle = document.getElementById("resultTitle");

const resultLiquid = document.getElementById("resultLiquid");
const precipitate = document.getElementById("precipitate");
const gas = document.getElementById("gas");

const observation = document.getElementById("observation");
const equation = document.getElementById("equation");
const explanation = document.getElementById("explanation");

const materialCount = document.getElementById("materialCount");
const pairHint = document.getElementById("pairHint");


// =========================================================
// DATA
// =========================================================

let materialsA = [];
let materialsB = [];


// =========================================================
// FIND MATERIAL
// =========================================================

function findMaterial(list, id) {
    return list.find(material => material.id === id);
}


// =========================================================
// UPDATE BOTTLE
// =========================================================

function updateBottle(selectElement, liquidElement, labelElement, formulaElement, pairElement, list) {

    const selectedId = selectElement.value;

    const selected = findMaterial(list, selectedId);

    if (!selected) {
        return;
    }

    liquidElement.style.background = selected.color;

    labelElement.textContent = selected.ar;

    formulaElement.textContent = selected.formula;

    pairElement.textContent = `زوج ${selected.pair}`;
}


// =========================================================
// FILL SELECT
// =========================================================

function fillSelect(selectElement, list) {

    selectElement.innerHTML = "";

    list.forEach(material => {

        const option = document.createElement("option");

        option.value = material.id;

        option.textContent =
            `${material.ar} — ${material.formula}`;

        selectElement.appendChild(option);
    });
}


// =========================================================
// HIDE RESULT
// =========================================================

function hideResult() {

    resultSection.classList.add("hidden");

    precipitate.classList.remove("show");
    gas.classList.remove("show");

    observation.textContent = "";
    equation.textContent = "";
    explanation.textContent = "";
}


// =========================================================
// RESET VISUAL EFFECTS
// =========================================================

function resetEffects() {

    precipitate.classList.remove("show");
    gas.classList.remove("show");

    resultLiquid.style.background = "#eef8fb";
}


// =========================================================
// MIX MATERIALS
// =========================================================

async function mixMaterials() {

    const a = materialA.value;
    const b = materialB.value;

    if (!a || !b) {
        return;
    }

    mixButton.disabled = true;

    mixButton.textContent = "MIXING...";

    try {

        const response = await fetch("/api/mix", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                a: a,
                b: b
            })
        });


        const data = await response.json();


        if (!data.success) {

            alert(data.message || "حدث خطأ.");

            return;
        }


        // -------------------------
        // RESET RESULT
        // -------------------------

        resetEffects();


        // -------------------------
        // RESULT CONTENT
        // -------------------------

        resultTitle.textContent = data.title;

        observation.textContent = data.observation;

        equation.textContent = data.equation;

        explanation.textContent = data.explanation;

        resultLiquid.style.background = data.color;


        // -------------------------
        // PRECIPITATE
        // -------------------------

        if (data.precipitate) {
            precipitate.classList.add("show");
        }


        // -------------------------
        // GAS
        // -------------------------

        if (data.gas) {
            gas.classList.add("show");
        }


        // -------------------------
        // SHOW RESULT
        // -------------------------

        resultSection.classList.remove("hidden");


        // Scroll to result

        setTimeout(() => {

            resultSection.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });

        }, 100);

    }

    catch (error) {

        console.error(error);

        alert(
            "تعذر الاتصال بالخادم. تأكدي أن app.py يعمل."
        );

    }

    finally {

        mixButton.disabled = false;

        mixButton.textContent = "MIX";
    }
}


// =========================================================
// NEW EXPERIMENT
// =========================================================

function startNewExperiment() {

    hideResult();

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}


// =========================================================
// CHANGE EVENTS
// =========================================================

materialA.addEventListener("change", () => {

    updateBottle(
        materialA,
        liquidA,
        labelA,
        formulaA,
        pairNumberA,
        materialsA
    );

    hideResult();
});


materialB.addEventListener("change", () => {

    updateBottle(
        materialB,
        liquidB,
        labelB,
        formulaB,
        pairNumberB,
        materialsB
    );

    hideResult();
});


// =========================================================
// BUTTON EVENTS
// =========================================================

mixButton.addEventListener(
    "click",
    mixMaterials
);

newExperiment.addEventListener(
    "click",
    startNewExperiment
);


// =========================================================
// INITIALIZE GAME
// =========================================================

async function initializeGame() {

    try {

        // -------------------------
        // MATERIALS
        // -------------------------

        const materialsResponse =
            await fetch("/api/materials");

        const materialsData =
            await materialsResponse.json();


        materialsA = materialsData.A;

        materialsB = materialsData.B;


        // -------------------------
        // PAIRS
        // -------------------------

        const pairsResponse =
            await fetch("/api/pairs");

        const pairsData =
            await pairsResponse.json();


        pairHint.textContent =
            pairsData.hint;


        // -------------------------
        // COUNT
        // -------------------------

        materialCount.textContent =
            materialsData.count;


        // -------------------------
        // FILL SEPARATE LISTS
        // -------------------------

        fillSelect(
            materialA,
            materialsA
        );

        fillSelect(
            materialB,
            materialsB
        );


        // -------------------------
        // DEFAULT PAIR
        // -------------------------

        if (
            materialsA.length > 0 &&
            materialsB.length > 0
        ) {

            materialA.value =
                materialsA[0].id;

            materialB.value =
                materialsB[0].id;
        }


        // -------------------------
        // INITIAL BOTTLES
        // -------------------------

        updateBottle(
            materialA,
            liquidA,
            labelA,
            formulaA,
            pairNumberA,
            materialsA
        );

        updateBottle(
            materialB,
            liquidB,
            labelB,
            formulaB,
            pairNumberB,
            materialsB
        );


        hideResult();

    }

    catch (error) {

        console.error(error);

        alert(
            "لم نستطع تحميل المواد. تأكدي أن Flask يعمل."
        );
    }
}


// =========================================================
// START
// =========================================================

initializeGame();