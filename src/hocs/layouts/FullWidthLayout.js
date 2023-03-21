import { connect } from 'react-redux';
import Navbar from '../../components/navigation/Navbar';
import Footer from '../../components/navigation/Footer';

const FullWidthLayouts = ({children}) => {
    return (
        <>
        <Navbar/>
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="max-w-7xl mx-auto">
                {children}
            </div>
        </div>
        <Footer/>
        </>
    )
}

const mapStateToProps = state => ({

})

export default connect(mapStateToProps, {

})(FullWidthLayouts)

