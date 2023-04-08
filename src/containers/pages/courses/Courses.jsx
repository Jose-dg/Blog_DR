import FullWidthLayout from 'hocs/layouts/FullWidthLayout';
import React from 'react';
import { connect } from 'react-redux';

function Courses() {
    return (
        <FullWidthLayout>
            Courses
        </FullWidthLayout>
    );
}

const mapStateToProps = state => ({

})
export default connect(mapStateToProps,{

})(Courses);