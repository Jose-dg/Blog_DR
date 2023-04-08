import Footer from '../../components/navigation/Footer';
import Navbar from '../../components/navigation/Navbar';
import { useEffect } from 'react'
import { connect } from 'react-redux';
import { get_categories } from 'redux/actions/categories'
import { get_network_id, loadWeb3 } from 'redux/actions/web3'

const FullWidthLayouts = ({
    children, 
    categories,
    loadWeb3,
    get_network_id,
    account
}) => {

    useEffect(()=>{
        categories ? <></>:get_categories()

        if(localStorage.getItem('account')){
            loadWeb3()
        }
        if(window.ethereum){
            get_network_id()
        }
    },[])

    return (
        <>
        <Navbar account={account}/>
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* We've used 3xl here, but feel free to try other max-widths based on your needs */}
            <div className="max-w-7xl mx-auto">
                {/* Content goes here */}
                {children}
            </div>
        </div>
        <Footer/>
        </>
    )
}

const mapStateToProps = state => ({
    categories: state.categories.categories,
    account: state.web3.account
})

export default connect(mapStateToProps, {
    loadWeb3,
    get_network_id
})(FullWidthLayouts)

