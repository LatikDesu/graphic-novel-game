import React, {useEffect, useState} from "react";
import {useNavigate} from 'react-router-dom';
// import StartScreen from "./StartScreen";
// import startScreen from '../../assets/classroom.png';
import Button from "../buttons/Button";
import DarkButton from "../buttons/DarkButton";
// import GameScreen from "./GameScreen";
// import EndScreen from "./EndScreen";
import css from '../game/Game.module.css';
import classNames from 'classnames';

const Games = () => {

    // const savedScene = localStorage.getItem('currentScene') ?? 0;
    const navigate = useNavigate();
    const [currentScene, setCurrentScene] = useState(0);
    const [isAddStyle, setIsAddStyle] = useState(false);
    // const [currentWindowIndex, setCurrentWindowIndex] = useState(0); //для сохранения в локал текущего диалога
    const [currentDialog, setCurrentDialog] = useState(0);
    const [dialogues, setDialogues] = useState([]); // в этот массив придет dialogues

    useEffect(() => {
        // Получение данных из localStorage
        const savedScene = parseInt(localStorage.getItem('currentScene') ?? 0);
        if (savedScene) {
            setCurrentScene(savedScene);
        }
        console.log(savedScene);
    }, []);

    // useEffect(() => {
    //     const fetchData = async () => {
    //         try {
    //             const response = await fetch('https://latikdesu.art/api/dialog/', {
    //                 method: 'POST',
    //                 headers: {
    //                     'Content-Type': 'application/json',
    //                 },
    //                 body: JSON.stringify({start: '0', end: '0'}),
    //             });
    //             const data = await response.json();
    //             setDialogues(data.dialogues);
    //         } catch (error) {
    //             console.error(error);
    //         }
    //         setTimeout(() => {
    //             fetchData();
    //         }, 2000);
    //     };
    //
    //     fetchData();
    // }, []);

    useEffect(() => {
        fetch('http://localhost:8000/api/dialog/')
            .then(response => response.json())
            .then(data => setDialogues(data));
    }, []);

    useEffect(() => {
        const savedDialogues = localStorage.getItem('dialogues');
        if (savedDialogues) {
            setDialogues(JSON.parse(savedDialogues));
        }
        console.log(savedDialogues);
    }, []);

    useEffect(() => {
        localStorage.setItem('dialogues', JSON.stringify(dialogues));
    }, [dialogues]);


    // useEffect(() => {
    //     const client = new APIClient();
    //     client.get_dialogues('dialog/', {start: '0', end: '0'}).then(data => {
    //         setDialogues(data);
    //     })
    //         .catch((error) => {
    //             console.error(error);
    //         });
    // }, []);

    // useEffect(() => {
    //     const client = new APIClient();
    //     const fetchData = () => {
    //         client
    //             .get_dialogues('dialog/', {start: '0', end: '0'})
    //             .then((data) => {
    //                 setDialogues(data);
    //             })
    //             .catch((error) => {
    //                 console.error(error);
    //             });
    //     };
    //     fetchData();
    //     if (!dialogues || dialogues.length === 0) {
    //         fetchData();
    //     }
    //     const intervalId = setInterval(fetchData, 5000);
    //     return () => clearInterval(intervalId);
    // }, []);

    const handlePrevDialog = () => {
        let dialogLength = dialogues[currentScene].windows.length;

        if (currentDialog === 0 && currentScene !== 0) {
            setCurrentScene(currentScene - 1);
            dialogLength = dialogues[currentScene - 1].windows.length;
            setCurrentDialog(dialogLength - 1);
            return;
        }

        if (currentDialog === 0 && currentScene === 0) {
            return;
        }

        if (currentDialog < dialogLength) {
            setCurrentDialog(currentDialog - 1);
            // setIsAddStyle(true);
        }
    };

    const handleNextDialog = () => {
        const dialogLength = dialogues[currentScene].windows.length;
        const sceneLength = dialogues.length - 1;

        if (currentDialog < dialogLength - 1) {
            setCurrentDialog(currentDialog + 1);
            return;
            // setIsAddStyle(true);
        }

        if (currentScene === sceneLength) {

            console.log("Конец");
            localStorage.setItem("currentScene", '0')
            return;
        }

        setCurrentScene(currentScene + 1);
        localStorage.setItem("currentScene", currentScene + 1);
        console.log(localStorage);
        setCurrentDialog(0);
        setIsAddStyle(true);
    };

    return (
        <div>
            <div>
                <pre>{JSON.stringify(dialogues[currentScene].windows[currentDialog], null, 2)}</pre>
            </div>

            <div className={classNames(css.scene, isAddStyle ? 'css.sceneShow' : '')}>
                <img className={css.sceneImg} src={require('../../' + dialogues[currentScene].path_img)}
                     alt={dialogues[currentScene]?.name}/>
                <div className={css.backMain}>
                    <Button onClick={async event => {
                        navigate('/start')
                    }}>Главная страница</Button>
                </div>
                {dialogues[currentScene].windows[currentDialog].position == 'right' ? (
                    <div className={css.positionRight}>
                        <img className={css.positionChar}
                             src={require('../../' + dialogues[currentScene]?.widows[currentDialog].path_img)}
                             alt={dialogues[currentScene].windows[currentDialog].character}/>
                    </div>
                ) : (
                    <div className={css.positionLeft}>
                        <img className={css.positionChar}
                             src={require('../../' + dialogues[currentScene].windows[currentDialog].path_img)}
                             alt={dialogues[currentScene].windows[currentDialog].character}/>
                    </div>
                )
                }
                {/*    /!* <div className={css.positionRight}>*/}
                {/*    <img className={css.positionChar}
                 src={require('../../'+dialogues[currentScene]windows[currentDialog].path_img)} alt={dialogues[currentScene].windows[currentDialog].character}/>*/}
                {/*   </div>   *!/*/}
                <div className={css.window}>
                    <div
                        className={css.character}>{dialogues[currentScene].windows[currentDialog].character}</div>
                    <div className={css.message}>{dialogues[currentScene].windows[currentDialog].text}</div>
                    <div className={css.buttons}>
                        <DarkButton onClick={handlePrevDialog}>Назад</DarkButton>
                        <DarkButton onClick={handleNextDialog}>Далее</DarkButton>
                    </div>
                </div>
            </div>
        </div>
    );

};

export default Games;
