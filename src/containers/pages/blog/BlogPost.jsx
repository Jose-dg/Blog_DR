import { useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { connect } from 'react-redux'
import FullWidthLayout from 'hocs/layouts/FullWidthLayout';
import { get_blog } from 'redux/actions/blog';

function BlogPost() {

    const params = useParams()
    const slug = params.slug

    useEffect(()=>{
        get_blog()
    },[])

    return (
        <FullWidthLayout>
            BlogPost
        </FullWidthLayout>
    );
}

const mapStateToProps = state => ({
    // blog_list: state.blog.blog_list
})

export default connect(mapStateToProps,{
    get_blog,
    // get_blog_list_page
})(BlogPost);
