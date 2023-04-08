import {
    LOAD_WEB3_SUCCESS,
    LOAD_WEB3_FAIL,
    CREATE_USER_SUCCESS,
    CREATE_USER_FAIL,
    LOAD_NETWORK_SUCCESS,
    LOAD_NETWORK_FAIL,
    LOAD_GAS_SUCCESS,
    LOAD_GAS_FAIL
} from './types'

import axios from 'axios'
import { ethers } from 'ethers';
import Web3 from 'web3/dist/web3.min';
 

export const loadWeb3 = () => async dispatch => {
    if(window.ethereum) {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        localStorage.setItem('account', accounts[0]);
        dispatch({
            type: LOAD_WEB3_SUCCESS,
            payload:accounts[0]
        })
    } else if (window.web3) {
        window.web3 = new Web3(window.web3.currentProvider)
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        localStorage.setItem('account', accounts[0]);
        dispatch({
            type: LOAD_WEB3_SUCCESS,
            payload:accounts[0]
        })
    } else {
        dispatch({
            type: LOAD_WEB3_FAIL,
        })
    }
}

export const loginWeb3 = () => async dispatch => {

    const config = {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
    };

    if(window.ethereum) {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        localStorage.setItem('account', accounts[0]);
        dispatch({
            type: LOAD_WEB3_SUCCESS,
            payload:accounts[0]
        })
        const formData = new FormData()
        formData.append('account', accounts[0])

        try {
            const res = await axios.post(
                `${process.env.REACT_APP_API_URL}/api/user/create`,
                formData,
                config
            );

            if (res.status === 201) {
                dispatch({
                    type: CREATE_USER_SUCCESS,
                    payload: res.data
                });
            } else {
                dispatch({
                    type: CREATE_USER_FAIL
                });
            }
        } catch(err) {
            dispatch({
                type: CREATE_USER_FAIL
            });
        }

    } else if (window.web3) {
        window.web3 = new Web3(window.web3.currentProvider)
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        localStorage.setItem('account', accounts[0]);
        dispatch({
            type: LOAD_WEB3_SUCCESS,
            payload:accounts[0]
        })
        const formData = new FormData()
        formData.append('account', accounts[0])

        try {
            const res = await axios.post(
                `${process.env.REACT_APP_API_URL}/api/user/create`,
                formData,
                config
            );

            if (res.status === 201) {
                dispatch({
                    type: CREATE_USER_SUCCESS,
                    payload: res.data
                });
            } else {
                dispatch({
                    type: CREATE_USER_FAIL
                });
            }
        } catch(err) {
            dispatch({
                type: CREATE_USER_FAIL
            });
        }
        

    } else {
        dispatch({
            type: LOAD_WEB3_FAIL,
        })
    }
}

export const get_network_id = () => async dispatch => {
    if(window.ethereum){
        const netId = await window.ethereum.request({ method: 'eth_chainId' })
        const networkID = parseInt(netId)

        dispatch({
            type: LOAD_NETWORK_SUCCESS,
            payload:networkID
        })
    }else{
        dispatch({
            type: LOAD_NETWORK_FAIL,
            payload:false
        })
    }
}
