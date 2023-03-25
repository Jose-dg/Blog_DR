import { connect } from 'react-redux';
import Navbar from '../../components/navigation/Navbar';
import Footer from '../../components/navigation/Footer';

const FullWidthLayouts = ({children}) => {
    return (
        <>
        <Navbar/>
        {children}
        <Footer/>
        </>
    )
}

const mapStateToProps = state => ({

})

export default connect(mapStateToProps, {

})(FullWidthLayouts)

