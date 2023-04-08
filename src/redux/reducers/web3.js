import {
    LOAD_WEB3_SUCCESS,
    LOAD_WEB3_FAIL,
    LOAD_NETWORK_SUCCESS,
    LOAD_NETWORK_FAIL
} from '../actions/types'

const initialstate = {
    account: null,
    web3: null,
    network: null
}

export default function web3(state=initialstate, action){
    const { type, payload } = action;

    switch(type){
        case LOAD_NETWORK_SUCCESS:
            return {
                ...state,
                network: payload
            }
        
        case LOAD_WEB3_SUCCESS:
            return {
                ...state,
                account: payload
            }    
        case LOAD_WEB3_FAIL:
            return {
                ...state,
                web3: null
            }
        case LOAD_NETWORK_FAIL:
            return {
                ...state,
                network: null
            }
    
        default:
            return state
    }

}